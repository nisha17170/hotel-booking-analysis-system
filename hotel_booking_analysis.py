import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
total_booking=0
total_revenue=0
#part 1 file handling
booking=[]
try:
    with open("hotel_booking.csv",mode="r") as file:
            reader=csv.reader(file)
            filtered_booking=[]
            for row in reader:
             try:
                nights=int(row[4])
                price=int(row[5])
                total_booking+=1
                total_revenue+=price*nights
             except:
                 pass
             with open("filtered_booking.csv",mode="w",newline="")as export_file:
                 writer=csv.writer(export_file)
                 writer.writerow(["booking_id","customer_id","hotel_name","room_type","nights","price"])
                 for row in filtered_booking:
                    writer.writerrow(row)
             with open("report.txt","w") as report:
                 report.write("hotel booking report\n")
                 report.write("total booking={total_booking}\n")
                 report.write("total revenue={total_revenue}\n")
            print("report generated successfully")
            print("filtered data exported successfully")
except FileNotFoundError:
 print("file not found")
# part 2 menu driven
while True:
    print("HOTEL BOOKING SYSTEM")
    print("view all bookings")
    print("search booking")
    print("city report")
    print("revenue report")
    print("export data")
    print("exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        print("view all bookings")
    elif choice==2:
        print("search booking")
    elif choice==3:
        print("city report")
    elif choice==4:
        print("revenue report")
    elif choice==5:
        print("export data")
    elif choice==6:
        print("exit")
        break
    else:
        print("invalid choice")
#part 3 string operations
guest_name=["john","John","JOHN"]
search_name=input("enter a guest name:")
search_name=search_name.strip().lower()
for name in guest_name:
    temp=name.upper()
    temp=name.replace("o","O")
    if name.lower()==search_name:
        print(name)
# part 4 list and dictionaries
data=[]
with open("hotel_booking.csv",mode="r") as file:
    reader=csv.DictReader(file)
    for row in reader:
        record={
            "guest_name":row["guest_name"],
             "city":row["city"],
             "room_type":row["room_type"],
               }
        data.append(row)
city_count={}
for row in data:
    city=row["city"]
    if city in city_count:
        city_count[city]+=1
    else:
        city_count[city]=1
print(city_count)
room_count={}
for row in data:
    room=row["room_type"]
    if room in room_count:
        room_count[room]+=1
    else:
        room_count[room]=1
print(room_count)
guest_count={}
for row in data:
    guest=row["guest_name"]
    if guest in guest_count:
        guest_count[guest]+=1
    else:
        guest_count[guest]=1
    print(guest_count)
most_frequent_guest=max(guest_count,key=guest_count.get)
print("city_count:",city_count)
print("room_count:",room_count)
print("most_frequent_guest:",most_frequent_guest)
#part 5 numpy
nights=np.array([1,2,3,4,5])
price_per_night=np.array([32500,25000,55500,15500,43000])
rating=np.array([4.5,4.8,4.9,4.9,4.3])
average_nights=np.mean(nights)
print("average_nights:",average_nights)
highest_price=np.max(price_per_night)
print("highest_price:",highest_price)
lowest_price=np.min(price_per_night)
print("lowest_price:",lowest_price)
std_rating=np.std(rating)
print("std_rating:",std_rating)
normalized_price=(price_per_night-np.min(price_per_night))/(np.max(price_per_night)-np.min(price_per_night))
print("normalized_price:",normalized_price)
average_price=np.mean(price_per_night)
above_average_price=price_per_night[price_per_night>average_price]
print("booking with above average price:",above_average_price)
# part 6 pandas
# Load CSV
df = pd.read_csv("hotel_booking.csv")
# -------------------------
# DATA INSPECTION
# -------------------------
print("HEAD")
print(df.head())
print("\nTAIL")
print(df.tail())
print("\nINFO")
print(df.info())
print("\nDESCRIBE")
print(df.describe())
# -------------------------
# FILTERING
# -------------------------
print("\nSuite Rooms")
print(df[df["room_type"] == "Suite"])
print("\nBookings from Chennai")
print(df[df["city"] == "Chennai"])
print("\nRatings Above 4.5")
print(df[df["rating"] > 4.5])
# -------------------------
# SORTING
# -------------------------
print("\nPrice Ascending")
print(df.sort_values(by="price_per_night"))
print("\nPrice Descending")
print(df.sort_values(by="price_per_night", ascending=False))
print("\nRating Descending")
print(df.sort_values(by="rating", ascending=False))
# GroupBy Analysis
# -------------------------
# Revenue by City
print("\nRevenue by City:")
df["revenue"] = df["night"] * df["price_per_night"]
print(df.groupby("city")["revenue"].sum())
# Revenue by Room Type
print("\nRevenue by Room Type:")
print(df.groupby("room_type")["revenue"].sum())
# Average Rating by City
print("\nAverage Rating by City:")
print(df.groupby("city")["rating"].mean())
# Discounted Price (10% Discount)
df["discounted_price"] = df["price_per_night"] * 0.90
print("\nData with New Columns:")
print(df[["price_per_night", "discounted_price", "revenue"]].head())
# Missing Values
# -------------------------
# Add missing values intentionally
df.loc[2, "rating"] = None
df.loc[5, "price_per_night"] = None
print("\nMissing Values:")
print(df.isnull().sum())
# Fill missing values
df_filled = df.fillna({
    "rating": df["rating"].mean(),
    "price_per_night": df["price_per_night"].mean()
})
print("\nAfter fillna():")
print(df_filled.head())
# Drop missing values
df_dropped = df.dropna()
print("\nAfter dropna():")
print(df_dropped.head())
# -------------------------
# Part 7 : Advanced Analysis
# -------------------------
# Top 5 Guests Based on Total Spending
top_guests = (
    df.groupby("guest_name")["revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)
print("\nTop 5 Guests:")
print(top_guests)
# Most Profitable City
city_revenue = (
    df.groupby("city")["revenue"]
    .sum()
    .sort_values(ascending=False)
)
print("\nMost Profitable City:")
print(city_revenue)
print("Highest Revenue City:", city_revenue.idxmax())
# Most Popular Room Type
popular_room = (
    df["room_type"]
    .value_counts()
)
print("\nMost Popular Room Type:")
print(popular_room)
print("Most Popular:", popular_room.idxmax())
# -------------------------
# Occupancy Report
# -------------------------
occupancy_report = (
    df.groupby("room_type")
    .size()
    .reset_index(name="Bookings")
)
print("\nOccupancy Report")
print(occupancy_report)
# -------------------------
# 1. Revenue by City (Bar Chart)
# -------------------------
city_revenue = df.groupby("city")["revenue"].sum()
plt.figure(figsize=(8,5))
plt.bar(city_revenue.index, city_revenue.values)
plt.xlabel("City")
plt.ylabel("Revenue")
plt.title("Revenue by City")
plt.show()
# -------------------------
# 2. Room Type Distribution (Pie Chart)
# -------------------------
room_counts = df["room_type"].value_counts()
plt.figure(figsize=(6,6))
plt.pie(room_counts,
        labels=room_counts.index,
        autopct="%1.1f%%")
plt.title("Room Type Distribution")
plt.show()
# -------------------------
# 3. Ratings Distribution (Histogram)
# -------------------------
plt.figure(figsize=(8,5))
plt.hist(df["rating"],
         bins=5)
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.title("Ratings Distribution")
plt.show()
# -------------------------
# 4. Revenue Trend (Line Chart)
# -------------------------
plt.figure(figsize=(8,5))
plt.plot(df["booking_id"],
         df["revenue"],
         marker='o')
plt.xlabel("Booking ID")
plt.ylabel("Revenue")
plt.title("Revenue Trend")
plt.savefig("Booking_analysis_graph.png")
plt.show()





