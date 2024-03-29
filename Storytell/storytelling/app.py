import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Actual data
ph_data = pd.DataFrame({
    'educ': [1, 1, 2, 3, 3, 3, 2, 2, 1, 1, 3, 3, 2, 2, 2, 1, 1, 1],
    'fin9': [1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1]
})

# Function to plot distribution of education levels
def plot_education_distribution():
    plt.figure(figsize=(10, 6))
    sns.countplot(data=ph_data, x='educ')
    plt.title('Distribution of Education Levels')
    plt.xlabel('Education Level')
    plt.ylabel('Count')
    st.pyplot()

# Function to perform correlation analysis
def correlation_analysis():
    # Create a pivot table to analyze the relationship between education level and making deposits
    education_deposit_pivot = pd.DataFrame({
        'Education Level': ['No education', 'Primary', 'Secondary', 'Tertiary'],
        'Percentage of Respondents Making Deposits': [0, 0, 23.44, 68.84]  # Provided percentages
    })

    # Display the pivot table
    st.write('Percentage of Respondents Making Deposits by Education Level')
    st.write(education_deposit_pivot)

    # Visualize the pivot table
    plt.figure(figsize=(10, 6))
    sns.barplot(data=education_deposit_pivot, x='Education Level', y='Percentage of Respondents Making Deposits')
    plt.title('Percentage of Respondents Making Deposits by Education Level')
    plt.xlabel('Education Level')
    plt.ylabel('Percentage of Respondents Making Deposits')
    plt.xticks(rotation=45)
    st.pyplot()

# Main function to run the Streamlit app
def main():
    # Page title
    st.title('Understanding the Relationship Between Education and Financial Inclusion')

    # Sidebar menu
    menu = ['Introduction', 'Methodology', 'Educational Background Analysis', 'Correlation Analysis', 'Conclusion/Recommendation']
    choice = st.sidebar.selectbox('Menu', menu)

    # Introduction section
    if choice == 'Introduction':
        st.markdown("""
        - Our project aimed to analyze the distribution of educational levels among respondents and investigate the correlation between education and financial inclusion indicators.
        - Understanding the correlation between education and financial inclusion is crucial for tailoring outreach programs.
        - Insights gained can inform resource allocation, product development, and outreach strategies, ultimately enhancing financial inclusion efforts and organizational impact.
           
        """)

    # Methodology section
    elif choice == 'Methodology':
        st.subheader('Methodology')
        st.image("./Methology/Method.png")

    # Conclusion/Recommendation section
    elif choice == 'Conclusion/Recommendation':
        st.subheader('Conclusion/Recommendation')
        st.markdown("""
            - **Conclusion:** The analysis highlights the significant role of education in financial behavior.
            - **Recommendation:** Insights suggest targeting financial education initiatives towards demographics with lower education levels. Additionally, tailor product offerings and outreach strategies to cater to diverse educational backgrounds.
            - **Action:** Implement targeted financial education programs and customize products to improve financial inclusion, thereby fostering economic empowerment.
        """)

    # Educational Background Analysis section
    elif choice == 'Educational Background Analysis':
        plot_education_distribution()
        st.markdown("""
            - **Education Level Distribution:** Most respondents had lower educational levels, with fewer respondents having higher education.
        """)

    # Correlation Analysis section
    elif choice == 'Correlation Analysis':
        correlation_analysis()
        st.markdown(""""
                    There's a noticeable correlation between education levels and making deposits into accounts. Respondents with higher education levels tend to make more deposits.
                    """)

if __name__ == '__main__':
    main()
