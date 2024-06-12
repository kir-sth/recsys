import pandas as pd
from sklearn.neighbors import NearestNeighbors

from app.models import Users


async def recommend_users(current_user: Users, all_users: list[Users], n_neighbors: int = 5):
    user_df = pd.DataFrame([{
        'id': user.id,
        'age': user.age,
        'gender': user.gender,
        'location': (user.latitude, user.longitude)  # Assuming this is a tuple for coordinates
    } for user in all_users])

    # Convert location to numerical value, like a combined coordinate or a quad_key
    user_df['location'] = user_df['location'].apply(lambda loc: loc[0] * 1e6 + loc[1])  # Example transformation

    features = ['age', 'location']
    
    model = NearestNeighbors(n_neighbors=n_neighbors)
    model.fit(user_df[features])

    current_user_location = current_user.latitude * 1e6 + current_user.longitude
    distances, indices = model.kneighbors(user_df[(user_df['id'] == current_user.id)][features])

    recommended_user_ids = user_df.iloc[indices[0]]['id'].values
    return recommended_user_ids
