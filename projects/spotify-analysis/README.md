# Spotify-Style Music Data Analysis

A reproducible beginner-friendly Python analysis of music features and popularity. **The dataset is synthetic, not downloaded from Spotify**, and the project does not claim real Spotify findings.

## Questions explored
- Which genres have the highest average popularity in this sample?
- Which tracks rank highest by popularity?
- How can music-feature data be summarized and visualized?

## Run locally
```bash
python analyze.py
```
To generate a chart:
```bash
pip install -r requirements.txt
python analyze.py
```

## Files
- `data/sample_tracks.csv` — 120 synthetic tracks with danceability, energy, genre, year, popularity, duration
- `analyze.py` — analysis script using Python's standard `csv` library; optional Matplotlib chart
- `outputs/genre_popularity.png` — generated chart
- `index.html` — public project overview

## Limitations
This is a teaching/demo dataset. It cannot support claims about actual Spotify listening habits, chart rankings, or platform trends. Replace it with appropriately licensed real data for a real-world analysis.

*Newly reconstructed in November 2026; not a recovered copy of the original project.*
