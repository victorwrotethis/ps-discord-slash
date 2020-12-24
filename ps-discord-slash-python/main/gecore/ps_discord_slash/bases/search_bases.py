from collections import namedtuple
import operator

from gecore.ps_discord_slash.models.base_query_result import BaseQueryResult

split_arg = ','
query_limit_single = 10
query_limit_multi = 5


def find_bases(bases, search_arg):
    query_result = BaseQueryResult()
    # Check for split arguments
    if split_arg in search_arg:
        multi_arg = search_arg.lower().split(split_arg)
        for arg in multi_arg:
            query_bases(bases, arg, query_result)
    else:
        query_bases(bases, search_arg, query_result)
    return query_result.bases


def query_bases(bases, search_query, query_result: BaseQueryResult):
    word_list = search_query.split()
    # Find bases from pool
    result_dict = search_bases(bases, search_query, word_list)
    # Filter bases
    if len(result_dict) < 1:
        query_result.bases.update({f'No Base Found for {search_query}': -1})
        return  # Early return to prevent filtering
    filter_bases(word_list, result_dict)
    # Update with latest results
    query_result.bases.update(result_dict)


def search_bases(bases, search_query, word_list) -> {}:
    result_dict = {}
    for base in bases:
        words_matching = 0
        for word in word_list:
            if word.lower() in base.lower():
                words_matching += 1
                if search_query == base.lower() or words_matching > 1:
                    return {base: bases[base]}
                else:
                    result_dict[base] = bases[base]
                    words_matching = 0
    return result_dict


def filter_bases(word_list, result_dict: {}):
    """""Grades the amount matching words per base and filters out any that fall below the highest graded result"""
    result_grades = {}
    for base_result in list(result_dict.keys()):
        for word in word_list:
            if word.lower() in base_result.lower():
                if base_result in result_grades:
                    result_grades[base_result] += 1
                else:
                    result_grades[base_result] = 1
    # Perhaps split here into a new func?
    best_result = max(result_grades.items(), key=operator.itemgetter(1))[0]
    best_size = result_grades[best_result]
    for base, gradation in result_grades.items():
        if gradation < best_size:
            result_dict.pop(base)

