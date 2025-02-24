#hotel_booking

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("hotel_bookings.csv")
print(df.tail(10))

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("hotel_bookings.csv")
print(df.head(10))


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("hotel_bookings.csv")
print(df.shape)


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("hotel_bookings.csv")
print(df.info())

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("hotel_bookings.csv")
for col in df.describe(include= 'object').columns:
    print(col)
    print(df[col].unique())
    print('_'*50)


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("hotel_bookings.csv")
df.drop(['company','agent'], axis = 1, inplace = True)
df.dropna(inplace=True)


print(df.isnull().sum())


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("hotel_bookings.csv")
print(df.describe())


# ==================================================================================== #
#                            1. Hotel Type Preference
# ==================================================================================== #
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv("hotel_bookings.csv")
plt.figure(figsize=(8, 5))
sns.countplot(x='hotel', data=df, palette='viridis')
plt.title("1. Hotel Type Preference", fontsize=16, fontweight='bold', color='darkblue')
plt.xlabel("Hotel Type", fontsize=12, fontweight='bold', color='black')
plt.ylabel("Number of Bookings", fontsize=12, fontweight='bold', color='black')
plt.show()

# ==================================================================================== #
#                             2. Monthly Bookings Trend
# ==================================================================================== #
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv("hotel_bookings.csv")
# convert to in datetime format
df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])

df['arrival_date_year'] = df['reservation_status_date'].dt.year

plt.figure(figsize=(12, 6))
sns.countplot(x='arrival_date_month', hue='arrival_date_year', data=df, 
              order=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], 
              palette='coolwarm')

plt.title("2. Monthly Bookings Trend (Year-wise)", fontsize=16, fontweight='bold', color='darkblue')
plt.xlabel("Month", fontsize=12, fontweight='bold', color='black')
plt.ylabel("Number of Bookings", fontsize=12, fontweight='bold', color='black')
plt.xticks(rotation=30)
plt.legend(title="Year")
plt.show()

# ==================================================================================== #
#                         3. Lead Time Distribution
# ==================================================================================== #
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv("hotel_bookings.csv")
plt.figure(figsize=(12, 5))
df['lead_time_category'] = pd.cut(df['lead_time'], bins=[0, 30, 60, 90, 180, 365, df['lead_time'].max()], 
                                  labels=["0-30", "31-60", "61-90", "91-180", "181-365", "365+"])

sns.countplot(x='lead_time_category', data=df, palette='viridis')
plt.title("3. Lead Time Distribution (Count of Bookings)", fontsize=16, fontweight='bold', color='darkblue')
plt.xlabel("Lead Time (Days)", fontsize=12, fontweight='bold', color='black')
plt.ylabel("Number of Bookings", fontsize=12, fontweight='bold', color='black')
plt.show()

# ==================================================================================== #
#                          4. Market Segment Distribution
# ==================================================================================== #
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv("hotel_bookings.csv")
plt.figure(figsize=(10, 5))
sns.countplot(x='market_segment', data=df, palette='viridis')
plt.title("4. Market Segment Distribution", fontsize=16, fontweight='bold', color='darkblue')
plt.xlabel("Market Segment", fontsize=12, fontweight='bold', color='black')
plt.ylabel("Number of Bookings", fontsize=12, fontweight='bold', color='black')
plt.xticks(rotation=30)
plt.show()

# ==================================================================================== #
#                              5. Booking Cancellation Rate
# ==================================================================================== #
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv("hotel_bookings.csv")
plt.figure(figsize=(6, 6))
df['is_canceled'].value_counts().plot.pie(autopct='%1.1f%%', labels=['Not Canceled', 'Canceled'], colors=['lightgreen', 'red'])
plt.title("5. Booking Cancellation Rate", fontsize=16, fontweight='bold', color='darkblue')
plt.show()

# ==================================================================================== #
#                             6. Deposit Type vs Cancellation
# ==================================================================================== #
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv("hotel_bookings.csv")
plt.figure(figsize=(8, 5))
sns.countplot(x='deposit_type', hue='is_canceled', data=df, palette='viridis')
plt.title("6. Deposit Type vs Cancellation", fontsize=16, fontweight='bold', color='darkblue')
plt.xlabel("Deposit Type", fontsize=12, fontweight='bold', color='black')
plt.ylabel("Number of Bookings", fontsize=12, fontweight='bold', color='black')
plt.legend(["Not Canceled", "Canceled"])
plt.show()

# ==================================================================================== #
#                           7. ADR by Hotel Type
# ==================================================================================== #
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv("hotel_bookings.csv")
plt.figure(figsize=(10, 5))
df['adr_range'] = pd.cut(df['adr'], bins=[0, 50, 100, 150, 200, 300, 500], labels=['0-50', '51-100', '101-150', '151-200', '201-300', '301-500'])
sns.countplot(x='adr_range', hue='hotel', data=df, palette='coolwarm')
plt.title("7. Count of Bookings by ADR Range and Hotel Type", fontsize=16, fontweight='bold', color='darkblue')
plt.xlabel("ADR Range", fontsize=12, fontweight='bold', color='black')
plt.ylabel("Number of Bookings", fontsize=12, fontweight='bold', color='black')
plt.legend(title="Hotel Type")
plt.show()

# ==================================================================================== #
#                              8. Total Guests per Booking
# ==================================================================================== #
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv("hotel_bookings.csv")
plt.figure(figsize=(10, 5))
df['total_guests'] = df['adults'] + df['children'] + df['babies']
df['guest_category'] = pd.cut(df['total_guests'], bins=[0, 1, 2, 3, 4, 5, 10], labels=['1', '2', '3', '4', '5', '6+'])
sns.countplot(x='guest_category', data=df, palette='coolwarm')
plt.title("8. Count of Bookings by Total Guests", fontsize=16, fontweight='bold', color='darkblue')
plt.xlabel("Total Guests", fontsize=12, fontweight='bold', color='black')
plt.ylabel("Number of Bookings", fontsize=12, fontweight='bold', color='black')
plt.show()

# ==================================================================================== #
#                           9. Most Preferred Meal Type
# ==================================================================================== #
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv("hotel_bookings.csv")
plt.figure(figsize=(8, 5))
sns.countplot(x='meal', data=df, order=df['meal'].value_counts().index, palette='coolwarm')
plt.title("9. Most Preferred Meal Type", fontsize=16, fontweight='bold', color='darkblue')
plt.xlabel("Meal Type", fontsize=12, fontweight='bold', color='black')
plt.ylabel("Number of Bookings", fontsize=12, fontweight='bold', color='black')
plt.show()

# ==================================================================================== #
#                           10. Total Bookings Over Time
# ==================================================================================== #
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv("hotel_bookings.csv")
plt.figure(figsize=(12, 5))
df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])  # Ensure it's DateTime
df['month_year'] = df['reservation_status_date'].dt.to_period('M')  # Group by Month-Year
sns.countplot(x=df['month_year'].astype(str), data=df, palette='viridis')
plt.title("10. Total Bookings Per Month", fontsize=16, fontweight='bold', color='darkblue')
plt.xlabel("Month-Year", fontsize=12, fontweight='bold', color='black')
plt.ylabel("Number of Bookings", fontsize=12, fontweight='bold', color='black')
plt.xticks(rotation=45)
plt.show()

# ==================================================================================== #
#                          11. Country-wise Bookings
# ==================================================================================== #
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv("hotel_bookings.csv")
plt.figure(figsize=(12, 6))
sns.barplot(x=df['country'].value_counts().index[:10], y=df['country'].value_counts().values[:10])
plt.title("11. Top 10 Countries by Bookings", fontsize=16, fontweight='bold', color='darkblue')
plt.xlabel("Country", fontsize=12, fontweight='bold', color='black')
plt.ylabel("Number of Bookings", fontsize=12, fontweight='bold', color='black')
plt.xticks(rotation=30)
plt.show()

# ==================================================================================== #
#                          12. Booking Status Distribution
# ==================================================================================== #
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv("hotel_bookings.csv")
plt.figure(figsize=(8, 5))
sns.countplot(x='reservation_status', data=df, palette='viridis')
plt.title("12. Booking Status Distribution", fontsize=16, fontweight='bold', color='darkblue')
plt.xlabel("Reservation Status", fontsize=12, fontweight='bold', color='black')
plt.ylabel("Count", fontsize=12, fontweight='bold', color='black')
plt.show()

# ==================================================================================== #
#                               13. ADR vs Lead Time
# ==================================================================================== #
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv("hotel_bookings.csv")
plt.figure(figsize=(12, 5))

df['lead_time_category'] = pd.cut(df['lead_time'], bins=[0, 30, 60, 90, 180, 365, df['lead_time'].max()], 
                                  labels=["0-30", "31-60", "61-90", "91-180", "181-365", "365+"])

sns.countplot(x='lead_time_category', data=df, palette='coolwarm')
plt.title("13. Count of Bookings by Lead Time Category", fontsize=16, fontweight='bold', color='darkblue')
plt.xlabel("Lead Time (Days)", fontsize=12, fontweight='bold', color='black')
plt.ylabel("Number of Bookings", fontsize=12, fontweight='bold', color='black')
plt.show()

# ==================================================================================== #
#                             14. Cancellation Rate by Month
# ==================================================================================== #
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv("hotel_bookings.csv")
plt.figure(figsize=(10, 5))
sns.barplot(x=df['arrival_date_month'], y=df['is_canceled'], estimator=lambda x: sum(x) / len(x), order=[
    'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
plt.title("14. Cancellation Rate by Month", fontsize=16, fontweight='bold', color='darkblue')
plt.xlabel("Month", fontsize=12, fontweight='bold', color='black')
plt.ylabel("Cancellation Rate", fontsize=12, fontweight='bold', color='black')
plt.xticks(rotation=30)
plt.show()

# ==================================================================================== #
#                              15. Total Bookings vs Cancellations
# ==================================================================================== #
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv("hotel_bookings.csv")
plt.figure(figsize=(8, 5))
sns.countplot(x='hotel', hue='is_canceled', data=df, palette='viridis')
plt.title("15. Total Bookings vs Cancellations", fontsize=16, fontweight='bold', color='darkblue')
plt.xlabel("Hotel Type", fontsize=12, fontweight='bold', color='black')
plt.ylabel("Number of Bookings", fontsize=12, fontweight='bold', color='black')
plt.legend(["Not Canceled", "Canceled"])
plt.show()

# ==================================================================================== #
#                              16. Repeated Customers per Hotel
# ==================================================================================== #
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv("hotel_bookings.csv")
plt.figure(figsize=(8, 5))
sns.barplot(x='hotel', y='is_repeated_guest', data=df, estimator=lambda x: sum(x), palette='coolwarm')
plt.title("16. Repeated Customers per Hotel Type", fontsize=16, fontweight='bold', color='darkblue')
plt.xlabel("Hotel Type", fontsize=12, fontweight='bold', color='black')
plt.ylabel("Number of Repeated Guests", fontsize=12, fontweight='bold', color='black')
plt.show()

# ==================================================================================== #
#                             17. Special Requests Trend
# ==================================================================================== #
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv("hotel_bookings.csv")
plt.figure(figsize=(8, 5))
sns.countplot(x='total_of_special_requests', data=df, palette='coolwarm')
plt.title("17. Special Requests Trend", fontsize=16, fontweight='bold', color='darkblue')
plt.xlabel("Number of Special Requests", fontsize=12, fontweight='bold', color='black')
plt.ylabel("Number of Bookings", fontsize=12, fontweight='bold', color='black')
plt.show()

# ==================================================================================== #
#                           18. Booking Trends by Customer Type
# ==================================================================================== #
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv("hotel_bookings.csv")
plt.figure(figsize=(8, 5))
sns.countplot(x='customer_type', data=df, palette='viridis')
plt.title("18. Booking Trends by Customer Type", fontsize=16, fontweight='bold', color='darkblue')
plt.xlabel("Customer Type", fontsize=12, fontweight='bold', color='black')
plt.ylabel("Number of Bookings", fontsize=12, fontweight='bold', color='black')
plt.show()

# ==================================================================================== #
#                           19. Average Length of Stay by Hotel Type
# ==================================================================================== #
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv("hotel_bookings.csv")
plt.figure(figsize=(8, 5))
sns.barplot(x='hotel', y='total_stay', data=df, estimator=np.mean, palette='coolwarm')
plt.title("19. Average Length of Stay by Hotel Type", fontsize=16, fontweight='bold', color='darkblue')
plt.xlabel("Hotel Type", fontsize=12, fontweight='bold', color='black')
plt.ylabel("Total Stay (Nights)", fontsize=12, fontweight='bold', color='black')
plt.show()

# ==================================================================================== #
#                            20. ADR by Distribution Channel
# ==================================================================================== #
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv("hotel_bookings.csv")
plt.figure(figsize=(10, 5))
sns.barplot(x='distribution_channel', y='adr', data=df, estimator=np.mean, palette='coolwarm')
plt.title("20. ADR by Distribution Channel", fontsize=16, fontweight='bold', color='darkblue')
plt.xlabel("Distribution Channel", fontsize=12, fontweight='bold', color='black')
plt.ylabel("Average ADR", fontsize=12, fontweight='bold', color='black')
plt.xticks(rotation=30)
plt.show()