# Steps for processing data

1. Copy URL from file
2. Format uri
3. Read each playlist
   - Copy song name, artist, and uri


# Playlist Types
- Mix it up (Commines random list of songs from each person)
  - MIU Exceptions (Same as main, but has variants without people)
- Daily Rotation (Creates master playlist, then breaks it apart into multiple sequences)

# Playlist folder structure
- Bot
  - Master Mix it up
    - Everyone
    - Withouts
      - Without x
      - Without y
      - Without z & a
  - Daily Rotations
    - Day 1
      - Everyone
      - Withouts
        - Without x
        - Without y
        - Without z & a
    - Day 2
      - Everyone
      - Withouts
        - Without x
        - Without y
        - Without z & a
    - Day 3
      - Everyone
      - Withouts
        - Without x
        - Without y
        - Without z & a


# Playlist Variable structure
- Playlists
  - play1
    - song1
      - name
      - artist
      - id
    - song2
    - song3
  - play2
  - play3

# Algorithm

## Rotation

### Create randoms
1. Dup playlists into a active and secondary playlist
2. Take the smallest playlist and have the set be the split value
3. Copy # random songs to active and remove them from secondary
4. Repeat step 3 times

### Exceptions
1. Check for Exceptions
2. Don't include playlist in mix

### Mix
1. Create playlist from each set to 1 list
2. Randomly move songs around

### Dup Check
1. If same song is present remove dup
2. Add random song from Uni list