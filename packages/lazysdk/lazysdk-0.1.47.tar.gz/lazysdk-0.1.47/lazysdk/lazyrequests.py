#!/usr/bin/env python3
# coding = utf8
"""
@ Author : ZeroSeeker
@ e-mail : zeroseeker@foxmail.com
@ GitHub : https://github.com/ZeroSeeker
@ Gitee : https://gitee.com/ZeroSeeker
"""
import requests
import showlog
import time
from urllib import parse



def lazy_requests(
        method,
        url,
        retry_delay: int = 1,  # 重试延时
        retry_limit: int = -1,  # 重试次数限制，-1为无限制
        return_json: bool = True,  # 是否返回json数据

        ReadTimeout_retry: bool = True,  # 超时重试
        JSONDecodeError_retry: bool = True,  # 返回非json类型重试
        ConnectionError_retry: bool = True,  # 连接错误重试
        ChunkedEncodingError: bool = True,

        **kwargs
):
    """
    retry_delay: 重试延时时长，单位为秒，默认为1秒

    return_json: 返回json，为True时返回json，否则直接返回

    ReadTimeout_retry: 超时重试，为True会自动重试，否则不会自动重试
    JSONDecodeError_retry：返回类型为非json重试，为True会自动重试，否则不会自动重试
    """
    retry_count = 0
    while True:
        try:
            if return_json is True:
                return requests.request(
                    method=method,
                    url=url,
                    **kwargs
                ).json()
            else:
                return requests.request(
                    method=method,
                    url=url,
                    **kwargs
                )
        except requests.exceptions.ReadTimeout:
            if ReadTimeout_retry is True:
                retry_count += 1
                showlog.warning(f'ReadTimeout_retry，将在{retry_delay}秒后重试第{retry_count}次...')
                time.sleep(retry_delay)
        except requests.exceptions.JSONDecodeError:
            if JSONDecodeError_retry is True:
                retry_count += 1
                showlog.warning(f'JSONDecodeError_retry，将在{retry_delay}秒后重试第{retry_count}次...')
                time.sleep(retry_delay)
        except requests.exceptions.ConnectionError:  # 包含ProxyError
            if ConnectionError_retry is True:
                retry_count += 1
                showlog.warning(f'ConnectionError_retry，将在{retry_delay}秒后重试第{retry_count}次...')
                time.sleep(retry_delay)
        except requests.exceptions.ChunkedEncodingError:
            if ChunkedEncodingError is True:
                retry_count += 1
                showlog.warning(f'ChunkedEncodingError_retry，将在{retry_delay}秒后重试第{retry_count}次...')
                time.sleep(retry_delay)
        if retry_limit == 0:
            break
        elif retry_limit < 0:
            pass
        else:
            if retry_count > retry_limit:
                break
            else:
                pass


def cookie_2_dict(
        cookie_str: str
) -> dict:
    """
    将cookie str 转换为 dict
    """
    res = dict()
    cookie_str_unquote = parse.unquote(cookie_str.replace('+', '%20'))
    cookie_str_split = cookie_str_unquote.split(';')
    for each_split in cookie_str_split:
        each_split_split = each_split.strip().split('=', 1)
        res[each_split_split[0]] = each_split_split[1]
    return res
