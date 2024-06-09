import pandas as pd
from sklearn.neighbors import NearestNeighbors

from app.models import Users


async def recommend_users(current_user: Users, all_users: list[Users], n_neighbors: int = 5):
    user_df = pd.DataFrame([{
        'id': user.id,
        'age': user.age,
        'gender': user.gender,
        'location': user.location
    } for user in all_users])

    # Assuming location is some numerical value for simplicity, it can be latitude/longitude
    features = ['age', 'location']
    
    # Fit the model
    model = NearestNeighbors(n_neighbors=n_neighbors)
    model.fit(user_df[features])

    # Find the nearest neighbors
    distances, indices = model.kneighbors(user_df[user_df['id'] == current_user.id][features])

    # Get recommended users
    recommended_user_ids = user_df.iloc[indices[0]]['id'].values
    return recommended_user_ids
