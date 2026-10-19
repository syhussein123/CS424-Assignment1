import pandas as pd
import altair as alt

df = pd.read_csv("data/processed/commutes_clean.csv")

bins = [0, 15, 30, 45, 60, 75, 90, 200]
labels = ['0-15', '15-30', '30-45', '45-60', '60-75', '75-90', '90+']
df['duration_bucket_str'] = pd.cut(df['duration_minutes'], bins=bins, labels=labels).astype(str)

weather_dropdown = alt.binding_select(options=['All'] + df['weather'].dropna().unique().tolist(), name='Weather: ')

weather_select = alt.selection_point(fields=['weather'], bind=weather_dropdown, init=[{'weather': 'All'}])


scatter = alt.Chart(df).mark_circle(size=60).encode(
    x=alt.X('distance_miles:Q', title='Distance (Miles)'),
    y=alt.Y('duration_minutes:Q', title='Duration (Minutes)'),
    color=alt.condition(weather_select, 'mode_of_transportation:N', alt.value('lightgray')),
    tooltip=['day_of_week', 'mode_of_transportation', 'weather', 'duration_minutes', 'distance_miles']
).add_params( 
    weather_select
).properties(
    title="Distance vs Commute Time by Mode",
    width=400,
    height=350
)


heatmap = alt.Chart(df).mark_rect().encode(
    x=alt.X('weather:N', title='Weather'),
    y=alt.Y('duration_bucket_str:O', title='Commute Time (Minutes)', sort=labels),
    # This dims the cells that don't match the dropdown selection
    color=alt.condition(
        weather_select, 
        alt.Color('count():Q', title='Number of People'), 
        alt.value('lightgray') 
    )
).properties(
    title="Weather vs Commute Duration",
    width=400,
    height=350
)

dashboard = (scatter | heatmap).resolve_scale(color='independent')

dashboard.save('task5_dashboard.html')
print("Saved dashboard to task5_dashboard.html! Open it in your web browser.")