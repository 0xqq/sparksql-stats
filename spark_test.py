# coding: utf-8
import time
from paper.spark_paper import SparkPaper
from question.spark_question import SparkQuestion
from cognition.spark_cognition import SparkCognition


def run_sql_v():
    print('sql version')
    start_time = time.time()

    # paper
    # s_paper = SparkPaper()
    # paper_id = "0009f836-bd30-11e7-97d7-005056b23776"
    # paper_info = s_paper.get_paper_info(paper_id=paper_id)
    # print(paper_info.toJSON().collect())
    #
    # question
    s_questionv = SparkQuestion()
    diff_df = s_questionv.get_question_diff_distri_sqlv(faculty=3, subject=1)
    print(diff_df.toJSON().collect())

    question_freq = s_questionv.get_question_freq_top_n_sqlv(faculty=3,
                                                             subject=1)
    print(question_freq.toJSON().collect())

    # cognition
    s_cognitionv = SparkCognition()
    knowledge_df = s_cognitionv.get_knowledge_top_n_sqlv(faculty=3, subject=1)
    print(knowledge_df.toJSON().collect())

    knowledge_freq = s_cognitionv.get_knowledge_freq_top_n_sqlv(faculty=3,
                                                                subject=1)
    print(knowledge_freq.toJSON().collect())

    print(time.time() - start_time)


def run_broadcast():
    print('broadcast version')
    start_time = time.time()

    # paper
    # s_paper = SparkPaper()
    # paper_id = "0009f836-bd30-11e7-97d7-005056b23776"
    # paper_info = s_paper.get_paper_info(paper_id=paper_id)
    # print(paper_info.toJSON().collect())
    #
    # question
    s_question = SparkQuestion()
    diff_df = s_question.get_question_diff_distri(faculty=3, subject=1)
    print(diff_df.toJSON().collect())

    question_freq = s_question.get_question_freq_top_n(faculty=3, subject=1)
    print(question_freq.toJSON().collect())

    # cognition
    s_cognition = SparkCognition()
    knowledge_df = s_cognition.get_knowledge_top_n(faculty=3, subject=1)
    print(knowledge_df.toJSON().collect())

    knowledge_freq = s_cognition.get_knowledge_freq_top_n(faculty=3, subject=1)
    print(knowledge_freq.toJSON().collect())

    print(time.time() - start_time)


if __name__ == '__main__':
    # run_sql_v()
    run_broadcast()
