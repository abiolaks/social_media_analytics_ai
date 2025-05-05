import pandas as pd
import numpy as np
import random
from faker import Faker

fake = Faker()
np.random.seed(42)
random.seed(42)

n = 3000
platforms = ["Twitter", "Instagram", "LinkedIn", "Facebook"]
content_types = ["image", "reel", "text", "video"]
locations = ["US", "UK", "Nigeria", "India", "Germany"]
devices = ["mobile", "desktop", "tablet"]
campaigns = ["Summer Sale", "New Product Launch", "Brand Awareness", "Holiday Promo"]

data = {
    "platform": np.random.choice(platforms, n),
    "post_id": [f"POST{i:05}" for i in range(n)],
    "content_type": np.random.choice(content_types, n),
    "date_posted": pd.date_range(start="2024-01-01", periods=n, freq="H"),
    "likes": np.random.poisson(50, n),
    "comments": np.random.poisson(10, n),
    "shares": np.random.poisson(5, n),
    "saves": np.random.poisson(3, n),
    "retweets": np.random.poisson(4, n),
    "clicks": np.random.poisson(20, n),
    "views": np.random.randint(100, 10000, n),
    "impressions": np.random.randint(500, 20000, n),
    "reach": np.random.randint(300, 18000, n),
    "followers_at_time": np.random.randint(1000, 100000, n),
    "demographic_segment": np.random.choice(
        ["18-24", "25-34", "35-44", "45-54", "55+"], n
    ),
    "location": np.random.choice(locations, n),
    "device_type": np.random.choice(devices, n),
    "campaign_name": np.random.choice(campaigns, n),
    "ad_spend": np.round(np.random.uniform(0, 500, n), 2),
    "boosted": np.random.choice([True, False], n),
    "caption_text": [fake.sentence() for _ in range(n)],
    "hashtags": [f"#{fake.word()}, #{fake.word()}" for _ in range(n)],
    "link_clicked": np.random.choice([True, False], n),
    "video_duration": np.round(np.random.uniform(0, 180, n), 1),
}

df = pd.DataFrame(data)
df["engagement"] = df["likes"] + df["comments"] + df["shares"]
df["engagement_rate"] = df["engagement"] / df["impressions"]
df["click_through_rate"] = df["clicks"] / df["impressions"]
df["conversion_rate"] = df["link_clicked"].astype(int) / df["clicks"].replace(0, 1)

df.to_csv("./data/social_media_data.csv", index=False)
print("✅ social_media_data.csv generated successfully.")
