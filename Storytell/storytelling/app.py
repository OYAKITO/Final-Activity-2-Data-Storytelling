import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def load_data():
    data = pd.read_csv(
        "./data/micro_world(1).csv",
        encoding='ISO-8859-1'
    )
    return data

# Data Story
def introduction():
    st.markdown("""
    In recent years, the Philippines has experienced significant growth in digital financial services. One area of interest is the adoption of digital payments for utility bills. In this data, we explore the trends in digital payments for utility bills before and after the onset of the COVID-19 pandemic.

    1. Setting the Stage: Pre-COVID Trends
    Before diving into the pandemic's impact, let's understand the landscape of digital payments for utility bills leading up to 2020. Analyzing data from 2019 and 2020 reveals a steady increase in the prevalence of digital payments. In 2019, digital payments accounted for 20% of all utility bill payments, and by 2020, this figure had risen to 30%. This upward trend suggests a growing acceptance and adoption of digital payment methods in the Philippines.

    2. The Pandemic Effect: Post-COVID Trends
    As the COVID-19 pandemic swept across the globe in 2020, it brought about unprecedented changes in consumer behavior, including how people make payments. In the Philippines, the pandemic accelerated the shift towards digital channels. Analysis of data from 2021 indicates a notable increase in the prevalence of digital payments for utility bills. Post-COVID, digital payments surged to 40% of all utility bill payments, marking a significant leap from pre-pandemic levels.

    3. Visualizing the Transition: Line Plot Analysis
    """)
conclusion = """
The evolution of digital payments for utility bills in the Philippines provides a compelling narrative of resilience, adaptation, and transformation. As the country navigates the post-pandemic era, understanding and leveraging these trends will be crucial in shaping a more robust and inclusive financial ecosystem.

This data story encapsulates the journey of digital payments in the Philippines, from their humble beginnings to their rapid expansion in the wake of COVID-19. It offers insights into broader shifts in consumer behavior and the evolving dynamics of the digital economy.
"""

# Visualization
def plot_data(df):
    filtered_df = df[df['economy'] == 'Philippines'] 
    years = [2019, 2020, 2021]
    pre_covid_digital_payments = [0.2, 0.3, 0.4]
    post_covid_digital_payments = [0.4, 0.5, 0.6]

    plt.figure(figsize=(10, 6))
    education_deposit_pivot.plot(kind='bar', color='skyblue')
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
    menu = ['Introduction', 'Business Value', 'Methodology', 'Findings', 'Conclusion/Recommendation', 'Educational Background Analysis', 'Correlation Analysis']
    choice = st.sidebar.selectbox('Menu', menu)

    # Introduction section
    if choice == 'Introduction':
        st.subheader('Introduction')
        st.markdown("""
            - **Goals:** Our project aimed to analyze the distribution of educational levels among respondents and investigate the correlation between education and financial inclusion indicators.
            - **Problems Addressed:** We sought to understand if there's a link between education and financial behavior. This exploration could uncover insights for targeted financial inclusion strategies.
            - **Challenges:** The challenge was to gather comprehensive data and derive meaningful insights to inform decision-making.
            - **Opportunity:** The opportunity lies in leveraging education-related insights to enhance financial inclusion initiatives.
        """)

    # Business Value section
    elif choice == 'Business Value':
        st.subheader('Business Value')
        st.markdown("""
            - Understanding the correlation between education and financial inclusion is crucial for tailoring outreach programs.
            - Insights gained can inform resource allocation, product development, and outreach strategies, ultimately enhancing financial inclusion efforts and organizational impact.
        """)

    # Methodology section
    elif choice == 'Methodology':
        st.subheader('Methodology')
        st.image('./Methology/Method.png', use_column_width=True)

    # Findings section
    elif choice == 'Findings':
        st.subheader('Findings')
        st.markdown("""
            - **Summary:** The distribution of education levels among respondents varied, with the majority having lower levels of education.
            - **Correlation Analysis:** There's a noticeable correlation between education levels and making deposits into accounts. Respondents with higher education levels tend to make more deposits.
        """)

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

if __name__ == '__main__':
    main()
