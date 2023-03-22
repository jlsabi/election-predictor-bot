def predict_election(posts_df, candidate1, candidate2):
    candidate1_count = posts_df[posts_df['text'].str.contains(candidate1)].count()[0]
    candidate2_count = posts_df[posts_df['text'].str.contains(candidate2)].count()[0]

    if candidate1_count > candidate2_count:
        return f"{candidate1} is predicted to win the election."
    elif candidate2_count > candidate1_count:
        return f"{candidate2} is predicted to win the election."
    else:
        return "The election result is too close to call."
