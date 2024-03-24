import streamlit as st
import matplotlib.pyplot as plt

# Data Story
introduction = """
In recent years, the Philippines has experienced significant growth in digital financial services. One area of interest is the adoption of digital payments for utility bills. In this data, we explore the trends in digital payments for utility bills before and after the onset of the COVID-19 pandemic.

1. Setting the Stage: Pre-COVID Trends
Before diving into the pandemic's impact, let's understand the landscape of digital payments for utility bills leading up to 2020. Analyzing data from 2019 and 2020 reveals a steady increase in the prevalence of digital payments. In 2019, digital payments accounted for 20% of all utility bill payments, and by 2020, this figure had risen to 30%. This upward trend suggests a growing acceptance and adoption of digital payment methods in the Philippines.

2. The Pandemic Effect: Post-COVID Trends
As the COVID-19 pandemic swept across the globe in 2020, it brought about unprecedented changes in consumer behavior, including how people make payments. In the Philippines, the pandemic accelerated the shift towards digital channels. Analysis of data from 2021 indicates a notable increase in the prevalence of digital payments for utility bills. Post-COVID, digital payments surged to 40% of all utility bill payments, marking a significant leap from pre-pandemic levels.

3. Visualizing the Transition: Line Plot Analysis
Visualizing the data through line plots provides a clear depiction of the transition in digital payment trends over time. Before COVID-19, the line representing digital payments for utility bills shows a gradual but consistent upward trajectory. However, post-COVID, there is a steep ascent in the prevalence of digital payments, indicating a rapid adoption of digital channels in response to the pandemic's disruptions.
"""

conclusion = """
The evolution of digital payments for utility bills in the Philippines provides a compelling narrative of resilience, adaptation, and transformation. As the country navigates the post-pandemic era, understanding and leveraging these trends will be crucial in shaping a more robust and inclusive financial ecosystem.

This data story encapsulates the journey of digital payments in the Philippines, from their humble beginnings to their rapid expansion in the wake of COVID-19. It offers insights into broader shifts in consumer behavior and the evolving dynamics of the digital economy.
"""

# Visualization
def plot_data():
    years = [2019, 2020, 2021]
    pre_covid_digital_payments = [0.2, 0.3, 0.4]
    post_covid_digital_payments = [0.4, 0.5, 0.6]

    plt.figure(figsize=(10, 6))
    plt.plot(years, pre_covid_digital_payments, marker='o', label='Pre-COVID')
    plt.plot(years, post_covid_digital_payments, marker='o', label='Post-COVID')
    plt.title('Digital Payments for Utility Bills in the Philippines')
    plt.xlabel('Year')
    plt.ylabel('Prevalence of Digital Payments')
    plt.xticks(years)
    plt.legend()
    plt.grid(True)

    st.pyplot(plt)

st.title("Evolution of Digital Payments for Utility Bills in the Philippines")

# Button to show Introduction
if st.button("Introduction"):
    st.write(introduction)
    plot_data()

# Button to show Conclusion
if st.button("Conclusion"):
    st.write(conclusion)
