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
- [JeffHoogland's pypair](https://github.com/JeffHoogland/pypair), using [NetworkX](https://networkx.github.io/) for matching
- Flask
- Heroku
- [Spice API](https://github.com/Utagai/spice)