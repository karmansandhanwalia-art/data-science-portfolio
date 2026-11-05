"""Explore an explicitly synthetic, Spotify-style sample dataset."""
from pathlib import Path
import csv
from collections import defaultdict
ROOT = Path(__file__).resolve().parent
with (ROOT / "data" / "sample_tracks.csv").open(newline="", encoding="utf-8") as handle:
    tracks = list(csv.DictReader(handle))
if not tracks:
    raise ValueError("No tracks found")
by_genre = defaultdict(list)
for track in tracks:
    by_genre[track["genre"]].append(track)
print(f"Total tracks: {len(tracks)}")
print("Average popularity by genre:")
for genre, group in sorted(by_genre.items()):
    mean = sum(float(t["popularity"]) for t in group) / len(group)
    print(f"  {genre:12s} {mean:.1f} ({len(group)} tracks)")
print("\nTop five tracks by popularity:")
for t in sorted(tracks, key=lambda t: float(t["popularity"]), reverse=True)[:5]:
    print(f"  {t['track']} — {t['artist']}: {t['popularity']}")
try:
    import matplotlib.pyplot as plt
except ImportError:
    print("Install matplotlib to create a chart: pip install matplotlib")
else:
    genres = sorted(by_genre)
    values = [sum(float(t["popularity"]) for t in by_genre[g]) / len(by_genre[g]) for g in genres]
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(genres, values)
    ax.set(title="Mean popularity by genre (synthetic data)", ylabel="Mean popularity score", xlabel="Genre")
    fig.tight_layout()
    destination = ROOT / "outputs" / "genre_popularity.png"
    fig.savefig(destination, dpi=150)
    print(f"\nChart saved to {destination}")
