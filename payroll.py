import math

days = int(input("出勤日数を入力して下さい:"))
HourlyWage = int(input("時給を入力して下さい:"))

timelist = []
moneylist = []

for i in range(days):
   StartTime = float(input("出勤時刻を入力してください:"))
#    StartTime = float(StartTimef)
   EndTime = int(input("退勤時刻を入力してください:"))

   if EndTime > StartTime:
      WorkingHours = EndTime - StartTime
      minutes = WorkingHours * 60
      t = WorkingHours//2

      if WorkingHours < 6:
         money = WorkingHours * HourlyWage
         timelist.append(WorkingHours)
         moneylist.append(money)
         print("勤務時間は" + str(WorkingHours) + "時間です")
         print("日給は" + str(money) +"円です")
         print("*****************************************")
         print("合計勤務時間は" + str(sum(timelist)) + "時間です")
         print("合計給料は" + str(sum(moneylist)) + "円です")
         print("=========================================")

      elif WorkingHours <= 6:
           k = t * 10
           difference = minutes - k
           WorkingTime = difference / 60
           money = WorkingTime * HourlyWage
           timelist.append(WorkingTime)
           moneylist.append(money)  
           print("勤務時間は" + str(WorkingTime) + "時間です")
           print("日給は" + str(money) +"円です")
           print("*****************************************")
           print("合計勤務時間は" + str(sum(timelist)) + "時間です")
           print("合計給料は" + str(sum(moneylist)) + "円です")
           print("=========================================")

      


      elif WorkingHours > 6:
           k = t * 10 + 20
           difference = minutes - k
           WorkingTime = difference / 60
           money = WorkingTime * HourlyWage
           timelist.append(WorkingTime)
           moneylist.append(money)
           print("勤務時間は" + str(WorkingTime) + "時間です")
           print("日給は" + str(money) +"円です")
           print("*****************************************")
           print("合計勤務時間は" + str(sum(timelist)) + "時間です")
           print("合計給料は" + str(sum(moneylist)) + "円です")
           print("=========================================")

      else:
          print("正しい数字を入力して下さい")

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
            print("勤務時間は" + str(WorkingTime) + "時間です")
            print("日給は" + str(money) +"円です")
            print("*****************************************")
            print("合計勤務時間は" + str(sum(timelist)) + "時間です")
            print("合計給料は" + str(sum(moneylist)) + "円です")
            print("=========================================")

         elif WorkingHours > 6:
              k = t * 10 + 20
              difference = minutes - k
              WorkingTime = difference / 60
              money = WorkingTime * HourlyWage
              timelist.append(WorkingTime)
              moneylist.append(money)
              print("勤務時間は" + str(WorkingTime) + "時間です")
              print("日給は" + str(money) +"円です")
              print("*****************************************")
              print("合計勤務時間は" + str(sum(timelist)) + "時間です")
              print("合計給料は" + str(sum(moneylist)) + "円です")
              print("=========================================")

         elif WorkingHours == 0:
              print("勤務時間に誤りがあります")
         else:
              print("正しい数字を入力して下さい")

   
   else:
        print("エラー")

sumTime = sum(timelist)
sumMoney = sum(moneylist)

print("切り上げた場合の合計時間は" + str(math.ceil(sumTime)) + "時間です")
print("切り上げた場合の合計給料は" + str(math.ceil(sumMoney)) + "円です")
