import os
import re
import json
from typing import (
    List,
    Dict,
    Literal,
    Optional
)
import requests
import pandas as pd
import pkg_resources
from collections import defaultdict
from dotenv import load_dotenv
from dataclasses import dataclass
from mjjo import Log
from mjjo.library.data import (
    ADD_BJD_CHANGED_DICTIONARY,
    CORRECT_ERROR_BJD
)


@dataclass
class Bjd():


    def __init__(self):
        load_dotenv()
        self.api_base_url: str = "https://api.odcloud.kr/api"
        self.api_get_url: str = "/15063424/v1/uddi:257e1510-0eeb-44de-8883-8295c94dadf7" # https://www.data.go.kr/data/15063424/fileData.do#layer-api-guide API 목록 중 국토교통부_전국 법정동_20230710 GET
        # self.api_key: str = os.environ['BJD_API_KEY']
        self.api_key = None
        self.api_page: int = 0
        self.api_per_page: int = 1024
        self.bjd_api_dictionary: Dict[str, Dict[str, str]] = None
        self.bjd_api_df: pd.DataFrame = None
        self.output_sep: Literal['\t'] = '\t'
        self.output_encoding: str = 'utf-8'
        self.output_index: bool = False
        self.file_name_bjd = pkg_resources.resource_filename(
            "mjjo", 
            "data/bjd.txt"
        )
        self.file_name_bjd_current = pkg_resources.resource_filename(
            "mjjo", 
            "data/bjd_current.txt"
        )
        self.file_name_bjd_changed = pkg_resources.resource_filename(
            "mjjo", 
            "data/bjd_changed.txt"
        )
        self.file_name_bjd_smallest = pkg_resources.resource_filename(
            "mjjo", 
            "data/bjd_smallest.txt"
        )
        self.file_name_bjd_frequency_dictionary = pkg_resources.resource_filename(
            "mjjo", 
            "data/bjd_frequency_dictionary.txt"
        )
        # self.file_path: str = f'{os.getcwd()}/mjjo/data'
        # self.file_name_bjd: str = f'{self.file_path}/bjd.txt'
        # self.file_name_bjd_current: str = f'{self.file_path}/bjd_current.txt'
        # self.file_name_bjd_changed: str = f'{self.file_path}/bjd_changed.txt'
        # self.file_name_bjd_smallest: str = f'{self.file_path}/bjd_smallest.txt'
        # self.file_name_bjd_frequency_dictionary: str = f'{self.file_path}/bjd_frequency_dictionary.txt'
        self.logger = Log('Bjd').stream_handler("INFO")
        self.add_bjd_changed_dictionary: Dict[str, str] = ADD_BJD_CHANGED_DICTIONARY
        self.correct_error_bjd: Dict[Dict[str, Optional[str]]] = CORRECT_ERROR_BJD

    @staticmethod
    def _request_api(api_url):
        return requests.get(api_url)

    @staticmethod
    def _convert_json(response):
        return json.loads(response.content)

    def _crawl_api(self) -> Dict[str, Dict[str, str]]:
        res_dic: Dict[str, Dict[str, str]] = dict()
        api_page = self.api_page
        while True:
            api_url = f"{self.api_base_url}{self.api_get_url}?page={api_page}&perPage={self.api_per_page}&serviceKey={self.api_key}"
            response = self._request_api(api_url)
            json_datas = self._convert_json(response)
            if json_datas['data']:
                self.logger.info(f"Crawling... {self.api_base_url}{self.api_get_url}?page={api_page}&perPage={self.api_per_page}")
                for data in json_datas['data']:
                    res_dic[f"{str(data['법정동코드'])}"] = {
                        '과거법정동코드': str(data['과거법정동코드']) if data['과거법정동코드'] is not None else None,
                        '리명': str(data['리명']) if data['리명'] is not None else None,
                        '법정동코드': str(data['법정동코드']) if data['법정동코드'] is not None else None,
                        '삭제일자': data['삭제일자'],
                        '생성일자': data['생성일자'],
                        '순위': data['순위'],
                        '시군구명': self._split_sgg_nm(str(data['시군구명'])) if data['시군구명'] is not None else None,
                        '시도명': str(data['시도명']) if data['시도명'] is not None else None,
                        '읍면동명': str(data['읍면동명']) if data['읍면동명'] is not None else None,
                    }
                api_page += 1
            else:
                break
        return res_dic

    def _correct_error(
        self,
        api_dic: Dict[str, Dict[str, str]]
    ):
        for cor_bjd_cd, cor_values in self.correct_error_bjd.items():
            for col_nm, cor_value in cor_values.items():
                api_dic[cor_bjd_cd][col_nm] = cor_value
        return api_dic

    @staticmethod
    def _split_sgg_nm(
        sgg_nm: Optional[str]
    ) -> Optional[str]:
        """
        시군구 행정구역명에서 시와 군 혹은 구가 결합되어있는 행정구역명을 분리하는 기능 \n
        조건에 부합하지 않을 경우 sgg_nm 을 그대로 반환한다
        
        - 조건 1: 결측값이 아님
        - 조건 2: 문자열수가 4개 이상
        - 조건 3: 마지막 문자열이 '구' 혹은 '군'
        - 조건 4: 첫번째와 마지막 문자열을 제외한 나머지 문자열 중 '시' 가 포함
        """

        if sgg_nm is not None \
        and len(sgg_nm) > 3 \
        and sgg_nm[-1] in ['구', '군'] \
        and '시' in sgg_nm[1:-1]:
            result = sgg_nm.split('시', 1)
            result[0] = result[0] + '시'
            return ' '.join(result)
        else:
            return sgg_nm

    @staticmethod
    def _clean_bjd_nm(
        bjd_nm: Optional[str]
    ) -> str:
        """
        행정구역명에서 한글과 숫자를 제외하고 삭제하는 기능 \n
        bjd_nm is None 일 경우 ''을 반환한다
        """

        if bjd_nm is not None:
            return re.sub(r'[^ 0-9ㄱ-ㅎ가-힣]+', '', bjd_nm)
        return ''

    def _get_full_bjd_nm(
        self,
        sido_nm: Optional[str],
        sgg_nm: Optional[str],
        emd_nm: Optional[str],
        ri_nm: Optional[str]
    ) -> str:
        """
        행정구역명을 결합하여 전체 법정동명을 생성하는 기능
        """

        sido_nm = self._clean_bjd_nm(sido_nm)
        sgg_nm = self._clean_bjd_nm(sgg_nm)
        emd_nm = self._clean_bjd_nm(emd_nm)
        ri_nm = self._clean_bjd_nm(ri_nm)

        full_bjd_nm = f'{sido_nm} {sgg_nm} {emd_nm} {ri_nm}'
        full_bjd_nm = full_bjd_nm.strip()  # 맨 앞과 맨 뒤의 공백 제거
        full_bjd_nm = re.sub(r'\s+', ' ', full_bjd_nm)  # 공백이 여러 칸인 것을 한 칸으로 변경
        return full_bjd_nm

    def _make_dataframe(self, res_dic) -> pd.DataFrame:
        res_df = pd.DataFrame(res_dic).T.sort_values('법정동코드').reset_index().drop(columns='index').replace(0, None).replace('0', None)
        res_df['시군구명'] = res_df['시군구명'].apply(lambda x: self._split_sgg_nm(x))
        res_df['법정동명'] = res_df[[
            '시도명',
            '시군구명',
            '읍면동명',
            '리명'
        ]].apply(lambda x: self._get_full_bjd_nm(*x), axis=1)
        return res_df
    
    def _create_bjd(self):
        """
        국토교통부 전국 법정동 API 수집하여 딕셔너리와 데이터프레임으로 가공하는 기능
        """

        res_dic = self._crawl_api()
        res_dic = self._correct_error(res_dic)
        res_df = self._make_dataframe(res_dic)
        self.bjd_api_dictionary = res_dic
        self.bjd_api_df = res_df
        self.logger.info("Success Created Bjd Dataframe and Dictionary from Public Data API")

    def _save_bjd(self):
        if self.bjd_api_df is None:
            self._create_bjd()
        self.bjd_api_df.to_csv(
            self.file_name_bjd,
            encoding=self.output_encoding,
            sep=self.output_sep,
            index=self.output_index
        )
        self.logger.info("Success Saved Bjd Dataframe To Text File")
        
    def _do_all_bjd_job(self):
        """
        국토교통부 전국 법정동 API 수집하여 법정동 관련 파일을 모두 생성하는 기능
        - bjd.txt
        - bjd_current.txt
        - bjd_changed.txt
        - bjd_smallest.txt
        - bjd_frequency_dictionary.txt
        """

        self._create_bjd()
        current_bjd = CurrentBjd()
        changed_bjd = ChangedBjd()
        smallest_bjd = SmallestBjd()
        bjd_frequency_dictionary = BjdFrequencyDictionary()

        current_bjd.bjd_api_df = self.bjd_api_df
        current_bjd.bjd_api_dictionary = self.bjd_api_dictionary
        current_bjd._create_current_bjd()
        changed_bjd.bjd_api_df = self.bjd_api_df
        changed_bjd.bjd_api_dictionary = self.bjd_api_dictionary
        changed_bjd._create_changed_bjd()
        
        smallest_bjd.bjd_api_df = self.bjd_api_df
        smallest_bjd.bjd_api_dictionary = self.bjd_api_dictionary
        smallest_bjd.current_bjd_df = current_bjd.current_bjd_df
        smallest_bjd._create_smallest_bjd()
        bjd_frequency_dictionary.bjd_api_df = self.bjd_api_df
        bjd_frequency_dictionary.bjd_api_dictionary = self.bjd_api_dictionary
        bjd_frequency_dictionary.current_bjd_df = current_bjd.current_bjd_df
        bjd_frequency_dictionary._create_bjd_frequency_dictionary()

        self._save_bjd()
        current_bjd._save_current_bjd()
        changed_bjd._save_changed_bjd()
        smallest_bjd._save_smallest_bjd()
        bjd_frequency_dictionary._save_bjd_frequency_dictionary()

@dataclass
class CurrentBjd(Bjd):

    def __init__(self):
        super().__init__()
        self.current_bjd_df: pd.DataFrame = None

    def _create_current_bjd(self):
        """
        국토교통부 전국 법정동 API 현재 존재하는 법정동만 데이터프레임으로 가공하는 기능
        """

        if self.bjd_api_df is None:
            self._create_bjd()
        self.current_bjd_df = self.bjd_api_df.loc[self.bjd_api_df['삭제일자'].isnull()]
        self.logger.info("Success Created Current Bjd Dataframe")

    def _save_current_bjd(self):
        if self.current_bjd_df is None:
            self._create_current_bjd()
        self.current_bjd_df.to_csv(
            self.file_name_bjd_current,
            encoding=self.output_encoding,
            sep=self.output_sep,
            index=self.output_index
        )
        self.logger.info("Success Saved Current Bjd Dataframe To Text File")

@dataclass
class ChangedBjd(Bjd):

    def __init__(self):
        super().__init__()
        self.changed_bjd_df: pd.DataFrame = None

    def _create_gangwon_prev_bjd_cd(
        self,
        sido_nm: str,
        prev_bjd_cd: str, # 법정동코드_변경전
        bjd_cd: str # 법정동코드_변경후
    ):
        if sido_nm == '강원특별자치도':
            return f'42{bjd_cd[2:]}'
        elif bjd_cd in self.add_bjd_changed_dictionary.keys():
            return self.add_bjd_changed_dictionary[bjd_cd]
        else:
            return prev_bjd_cd

    def _get_prev_bjd_nm(
        self,
        prev_bjd_cd: Optional[str] # 법정동코드_변경전
    ) -> str:
        if prev_bjd_cd is None:
            return None
        if prev_bjd_cd not in self.bjd_api_dictionary.keys():
            return None
        try:
            data = self.bjd_api_dictionary[prev_bjd_cd]
            sido_nm = data['시도명']
            sgg_nm = data['시군구명']
            emd_nm = data['읍면동명']
            ri_nm = data['리명']

            return self._get_full_bjd_nm(
                sido_nm,
                sgg_nm,
                emd_nm,
                ri_nm
            )
        except:
            return None

    def _get_prev_value(
        self,
        prev_bjd_cd: Optional[str], # 법정동코드_변경전
        value_nm: str
    ):
        if prev_bjd_cd is None:
            return None
        if prev_bjd_cd not in self.bjd_api_dictionary.keys():
            return None
        try:
            return self.bjd_api_dictionary[prev_bjd_cd][value_nm]
        except:
            return None

    @staticmethod
    def _find_diff(
        bjd_cd_curr: Optional[str], # 법정동코드_변경전
        bjd_cd_prev: Optional[str], # 법정동코드_변경후
        bjd_nm_curr: Optional[str], # 법정동명_변경전
        bjd_nm_prev: Optional[str] # 법정동명_변경후
    ) -> str:
        bjd_cd_changed = ''
        bjd_nm_changed = ''
        if bjd_cd_prev and bjd_cd_curr:
            if bjd_cd_prev != bjd_cd_curr:
                bjd_cd_changed = f'{bjd_cd_prev} > {bjd_cd_curr}'
        if bjd_nm_prev and bjd_nm_curr:
            changed_list_prev = list()
            changed_list_curr = list()
            for w1, w2 in zip(bjd_nm_prev.split(), bjd_nm_curr.split()):
                if w1 != w2:
                    changed_list_prev.append(w1)
                    changed_list_curr.append(w2)
            bjd_nm_changed = f"{' '.join(changed_list_prev)} > {' '.join(changed_list_curr)}"
        return f'[법정동코드 변경내역] {bjd_cd_changed} | [법정동명 변경내역]: {bjd_nm_changed}'

    def _create_changed_bjd(self):
        if self.bjd_api_df is None:
            self._create_bjd()
        self.changed_bjd_df = self.bjd_api_df.copy()
        self.changed_bjd_df = self.changed_bjd_df.rename(columns={
            '법정동코드': '법정동코드_변경후',
            '법정동명': '법정동명_변경후',
            '생성일자': '생성일자_변경후',
            '삭제일자': '삭제일자_변경후',
            '과거법정동코드': '법정동코드_변경전',
        })
        self.changed_bjd_df['법정동코드_변경전'] = self.changed_bjd_df[[
            '시도명',
            '법정동코드_변경전',
            '법정동코드_변경후'
        ]].apply(lambda x: self._create_gangwon_prev_bjd_cd(*x), axis=1)
        self.changed_bjd_df = self.changed_bjd_df[[
            '법정동코드_변경후',
            '법정동명_변경후',
            '생성일자_변경후',
            '삭제일자_변경후',
            '법정동코드_변경전'
        ]]
        self.changed_bjd_df = self.changed_bjd_df.loc[
            (self.changed_bjd_df['생성일자_변경후'] != self.changed_bjd_df['삭제일자_변경후']) &
            ~(self.changed_bjd_df['생성일자_변경후'] > self.changed_bjd_df['삭제일자_변경후'])
        ]
        self.changed_bjd_df = self.changed_bjd_df.loc[
            (self.changed_bjd_df['법정동코드_변경전'].isnull()==False) &
            (self.changed_bjd_df['법정동코드_변경전'].str.len() == 10)
        ].sort_values('생성일자_변경후')
        self.changed_bjd_df['법정동명_변경전'] = self.changed_bjd_df['법정동코드_변경전'].apply(lambda x: self._get_prev_bjd_nm(x))
        self.changed_bjd_df['생성일자_변경전'] = self.changed_bjd_df['법정동코드_변경전'].apply(lambda x: self._get_prev_value(x, '생성일자'))
        self.changed_bjd_df['삭제일자_변경전'] = self.changed_bjd_df['법정동코드_변경전'].apply(lambda x: self._get_prev_value(x, '삭제일자'))

        self.changed_bjd_df['변경내역'] = self.changed_bjd_df[[
            '법정동코드_변경후',
            '법정동코드_변경전', 
            '법정동명_변경후',
            '법정동명_변경전'
        ]].apply(lambda x: self._find_diff(*x), axis=1)
        self.changed_bjd_df = self.changed_bjd_df.sort_values(['생성일자_변경후'], na_position='first')
        self.logger.info("Success Created Changed Bjd Dataframe")
        
    def _save_changed_bjd(self):
        if self.changed_bjd_df is None:
            self._create_changed_bjd()
        self.changed_bjd_df.to_csv(
            self.file_name_bjd_changed,
            encoding=self.output_encoding,
            sep=self.output_sep,
            index=self.output_index
        )
        self.logger.info("Success Saved Changed Bjd Dataframe To Text File")

@dataclass
class SmallestBjd(CurrentBjd):

    def __init__(self):
        super().__init__()
        self.smallest_bjd_list: List[str] = None

    def _create_smallest_bjd(self):
        if self.current_bjd_df is None:
            self._create_current_bjd()
        smallest_bjd_set = set()
        for bjd in self.current_bjd_df['법정동명']:
            if bjd[-1] in ['가', '동', '로', '리']:
                smallest_bjd_set.add(bjd.split(' ')[-1])

        self.smallest_bjd_list = sorted(list(smallest_bjd_set))
        self.logger.info("Success Created Smallest Bjd Name List")

    def _save_smallest_bjd(self):
        if self.smallest_bjd_list is None:
            self._create_smallest_bjd()
        with open(self.file_name_bjd_smallest, 'w') as f:
            f.writelines('\n'.join(self.smallest_bjd_list))
            f.close()
        self.logger.info("Success Saved Changed Smallest Bjd Name List To Text File")

@dataclass
class BjdFrequencyDictionary(CurrentBjd):

    def __init__(self):
        super().__init__()
        self.bjd_frequency_dictionary: Dict[str, int] = None
        
    def _create_bjd_frequency_dictionary(self):
        if self.current_bjd_df is None:
            self._create_current_bjd()
        self.bjd_frequency_dictionary = defaultdict(int)
        for bjd in self.current_bjd_df['법정동명']:
            bjd_words = bjd.split(' ')
            for word in bjd_words:
                self.bjd_frequency_dictionary[word] += 1

        self.logger.info("Success Created Bjd Frequency Dictionary")

    def _save_bjd_frequency_dictionary(self):
        if self.bjd_frequency_dictionary is None:
            self._create_bjd_frequency_dictionary()
        bjd_frequency_list = list((key, value) for key, value in self.bjd_frequency_dictionary.items())
        with open(self.file_name_bjd_frequency_dictionary, 'w') as f:
            vstr = ''
            sep = ','
            for line in bjd_frequency_list:
                for s in line:
                    vstr = vstr + str(s) + sep
                vstr = vstr.rstrip(sep)  # 마지막에도 추가되는  sep을 삭제 
                vstr = vstr + '\n'
            f.writelines(vstr)  # 한 라인씩 저장 
            f.close()

        self.logger.info("Success Saved Bjd Frequency Dictionary To Text File")
