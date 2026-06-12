import pandas as pd

try:
    df = pd.read_csv("data.csv")
    print("✅ Dataset loaded successfully.")
    print("\n📊 First 5 rows:\n", df.head())

except FileNotFoundError:
    print("❌ CSV file not found.")
except Exception as e:
    print("❌ Error loading dataset:", e)


print("\n🔍 Dataset Info:")
print(df.info())

print("\n📈 Summary Statistics:")
print(df.describe())


df.fillna(df.mean(numeric_only=True), inplace=True)

df.drop_duplicates(inplace=True)

df.loc[df['Age'] < 0, 'Age'] = df['Age'].mean()

print("\n✅ Data cleaned successfully.")


high_salary = df[df['Salary'] > 50000]
print("\n💰 Employees with Salary > 50,000:\n", high_salary)


dept_salary = df.groupby("Department")["Salary"].mean()
print("\n🏢 Average Salary by Department:\n", dept_salary)

dept_count = df["Department"].value_counts()
print("\n👥 Employee Count by Department:\n", dept_count)

df.to_csv("cleaned_data.csv", index=False)
print("\n✅ Cleaned dataset saved as 'cleaned_data.csv'.")
