# anirank
Rank the anime in a user's MyAnimeList using a modified Swiss tournament system and a blossom algorithm.
Basic functionality has been proven in Python.
Roadmap:

Webpage interface functionality:
- Enter a MAL username to import their anime (or manga) list
- Filter anime list by status, type, etc
- Vote on items
- See results list

Backend functionality:
- Implement mattkrick's EdmondsBlossom javascript function
- Port JeffHoogland's pypair to javascript using EdmondsBlossom instead of networkx
- Port my own anirank python program to javascript
