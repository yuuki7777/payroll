import math

days = int(input("�o�Γ�������͂��ĉ�����:"))
HourlyWage = int(input("��������͂��ĉ�����:"))

timelist = []
moneylist = []

for i in range(days):
   StartTime = float(input("�o�Ύ�������͂��Ă�������:"))
#    StartTime = float(StartTimef)
   EndTime = int(input("�ދΎ�������͂��Ă�������:"))

   if EndTime > StartTime:
      WorkingHours = EndTime - StartTime
      minutes = WorkingHours * 60
      t = WorkingHours//2

      if WorkingHours < 6:
         money = WorkingHours * HourlyWage
         timelist.append(WorkingHours)
         moneylist.append(money)
         print("�Ζ����Ԃ�" + str(WorkingHours) + "���Ԃł�")
         print("������" + str(money) +"�~�ł�")
         print("*****************************************")
         print("���v�Ζ����Ԃ�" + str(sum(timelist)) + "���Ԃł�")
         print("���v������" + str(sum(moneylist)) + "�~�ł�")
         print("=========================================")

      elif WorkingHours <= 6:
           k = t * 10
           difference = minutes - k
           WorkingTime = difference / 60
           money = WorkingTime * HourlyWage
           timelist.append(WorkingTime)
           moneylist.append(money)  
           print("�Ζ����Ԃ�" + str(WorkingTime) + "���Ԃł�")
           print("������" + str(money) +"�~�ł�")
           print("*****************************************")
           print("���v�Ζ����Ԃ�" + str(sum(timelist)) + "���Ԃł�")
           print("���v������" + str(sum(moneylist)) + "�~�ł�")
           print("=========================================")

      


      elif WorkingHours > 6:
           k = t * 10 + 20
           difference = minutes - k
           WorkingTime = difference / 60
           money = WorkingTime * HourlyWage
           timelist.append(WorkingTime)
           moneylist.append(money)
           print("�Ζ����Ԃ�" + str(WorkingTime) + "���Ԃł�")
           print("������" + str(money) +"�~�ł�")
           print("*****************************************")
           print("���v�Ζ����Ԃ�" + str(sum(timelist)) + "���Ԃł�")
           print("���v������" + str(sum(moneylist)) + "�~�ł�")
           print("=========================================")

      else:
          print("��������������͂��ĉ�����")

   elif EndTime < StartTime:
         s = EndTime + 24
         WorkingHours = s - StartTime
         minutes = WorkingHours * 60
         t = WorkingHours//2

         if WorkingHours <= 6:
            k = t * 10
            difference = minutes - k
            WorkingTime = difference / 60
            money = WorkingTime * HourlyWage
            timelist.append(WorkingTime)
            moneylist.append(money)
            print("�Ζ����Ԃ�" + str(WorkingTime) + "���Ԃł�")
            print("������" + str(money) +"�~�ł�")
            print("*****************************************")
            print("���v�Ζ����Ԃ�" + str(sum(timelist)) + "���Ԃł�")
            print("���v������" + str(sum(moneylist)) + "�~�ł�")
            print("=========================================")

         elif WorkingHours > 6:
              k = t * 10 + 20
              difference = minutes - k
              WorkingTime = difference / 60
              money = WorkingTime * HourlyWage
              timelist.append(WorkingTime)
              moneylist.append(money)
              print("�Ζ����Ԃ�" + str(WorkingTime) + "���Ԃł�")
              print("������" + str(money) +"�~�ł�")
              print("*****************************************")
              print("���v�Ζ����Ԃ�" + str(sum(timelist)) + "���Ԃł�")
              print("���v������" + str(sum(moneylist)) + "�~�ł�")
              print("=========================================")

         elif WorkingHours == 0:
              print("�Ζ����ԂɌ�肪����܂�")
         else:
              print("��������������͂��ĉ�����")

   
   else:
        print("�G���[")

sumTime = sum(timelist)
sumMoney = sum(moneylist)

print("�؂�グ���ꍇ�̍��v���Ԃ�" + str(math.ceil(sumTime)) + "���Ԃł�")
print("�؂�グ���ꍇ�̍��v������" + str(math.ceil(sumMoney)) + "�~�ł�")
