import sys
import data
import statistics
import copy


def main(argv):

    # data setup
    records = data.load_data(argv[1], argv[2])
    q1_records = copy.deepcopy(records)

    # Question 1
    print("Question 1:")

    statistical_functions = [statistics.sum, statistics.mean, statistics.median]
    # print statistical indices for the summer
    features = ["hum", "t1", "cnt"]
    summer_records = data.filter_by_feature(q1_records, "season", {1})[0]
    print("Summer:")
    data.print_details(summer_records, features, statistical_functions)

    # print statistical indices for holiday
    holiday_records = data.filter_by_feature(q1_records, "is_holiday", {1})[0]
    print("Holiday:")
    data.print_details(holiday_records, features, statistical_functions)

    # print statistical indices for the entire population
    print("All:")
    data.print_details(q1_records, features,  statistical_functions)

    print("\n", end='')

    # Question 2
    print("Question 2:")

    # reset data from file
    # setup relevant records
    # filter data from seasons other than winter
    q2_pre_records = data.filter_by_feature(records, "season", {3})[0]
    # divide by 'is_holiday':
    # 'q2_records[0]' contains records of winter holidays
    # 'q2_records[1]' contains records of winter weekdays
    q2_records = data.filter_by_feature(q2_pre_records, "is_holiday", {1})

    threshold = 13.0
    funcs = [statistics.mean, statistics.median]

    # print population statistics for records with t1<=13.0
    print("If t1<=13.0, then:", end='\n')
    # print population statistics for winter holiday records
    statistics.population_statistics("Winter holiday records", q2_records[0], "t1", "cnt", threshold, False, funcs)
    # print population statistics for winter weekday records
    statistics.population_statistics("Winter weekday records", q2_records[1], "t1", "cnt", threshold, False, funcs)

    # print population statistics for records with t1>13.0
    print("If t1>13.0, then:", end='\n')
    # print population statistics for winter holiday records
    statistics.population_statistics("Winter holiday records", q2_records[0], "t1", "cnt", threshold, True, funcs)
    # print population statistics for winter weekday records
    statistics.population_statistics("Winter weekday records", q2_records[1], "t1", "cnt", threshold, True, funcs)


if __name__ == '__main__':
    main(sys.argv)
