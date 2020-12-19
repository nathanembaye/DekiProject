from datetime import timedelta
import numpy as np
from scipy.optimize import linear_sum_assignment as hungarianMethod
import pandas as pd

#load excel file of student and tutors subjects/available days+times
#note: study hours only 10am-7pm
#time is represented where 9am=0, 10am=1-->6pm=8, 7pm=9
students_excel = pd.read_excel("Data/SampleDekiData.xlsx", 'Students')
tutors_excel = pd.read_excel("Data/SampleDekiData.xlsx", 'Tutors')

def main():
  list_of_students = loadExcel(students_excel)
  list_of_tutors = loadExcel(tutors_excel)
  calculateCompatibility(list_of_students, list_of_tutors)

#counts number of common subjects
def calculate_subject_score(student_subjects, tutor_subjects):
  return len(np.intersect1d(student_subjects, tutor_subjects))

#counts number of common subjects
def calculate_date_score(student_date, tutor_date):
  return 0.25 * len(np.intersect1d(student_date, tutor_date))

#sum subject and availbility scores
def calculate_final_score(student_subject_score, student_date_score):
  return student_subject_score + student_date_score

#parition subject list for tutors/students
def parse_subjects(subjects):
  return subjects.split(",")

#partition avilabile days+times for tutors/students
def parse_dates(dates):

  if type(dates) == int:
    dates = str(dates)

  dates = dates.split(",")

  placeholder = []
  for i in range(0, len(dates)):

      dates[i] = timedelta(days=int(dates[i][0]), hours=int(dates[i][1]))
      placeholder.append(dates[i])

  return placeholder


def loadExcel(excel_data):

  placeholder1 = []

  #for number of excel rows in sheet
  for i in range(0, len(excel_data)):

    placeholder2 = {}

    #for number of excel columns in sheet
    for j in range(0, len(excel_data.columns)):

      #make list of subjects for every tutor or student
      if excel_data.columns[j] == "Subjects":
        placeholder2[excel_data.columns[j]] = parse_subjects(excel_data.loc[i].values.tolist()[j])

      # make list of available times/days for every tutor or student
      elif excel_data.columns[j] == "Dates":
        placeholder2[excel_data.columns[j]] = parse_dates(excel_data.loc[i].values.tolist()[j])

      #make name of every tutor or student a key in dictionary
      else:
        placeholder2[excel_data.columns[j]] = excel_data.loc[i].values.tolist()[j]

    #place tutor or student data in final list of data
    placeholder1.append(placeholder2)

  return placeholder1

#print final matches
def printMatches(list_of_students, list_of_tutors, x, y):

  print("--------------MATCHES--------------")

  #print optimized final tutor and student matches
  for match in range(0, len(x)):
     print("Student: " + list_of_students[x[match]]["Name"] + "      Tutor: " + list_of_tutors[y[match]]["Name"])

def calculateCompatibility(list_of_students, list_of_tutors):

  compatiblity_scores = []

  #iterate through student list
  for i in list_of_students:

    student_score = []

    #iterate through tutor list
    for j in list_of_tutors:


      #calculate student compatibility score with every tutor
      student_subject_score = calculate_subject_score(i["Subjects"], j["Subjects"])
      student_date_score = calculate_date_score(i["Dates"], j["Dates"])
      student_score.append(calculate_final_score(student_subject_score, student_date_score))

    #add list of computed scores
    compatiblity_scores.append(student_score)

  #find x,y combination in matrix for optimized compatiblity
  x, y = hungarianMethod(compatiblity_scores, True)
  printMatches(list_of_students, list_of_tutors, x, y)


main()