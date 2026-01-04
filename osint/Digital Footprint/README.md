# Digital Footprint

Author: [Claude](https://github.com/anthropics)

## Description

An OSINT challenge involving image analysis and location identification.

## Requirements

- Google Images / Reverse Image Search
- Google Maps
- EXIF viewer (optional)

## Sources

```
A suspect posted this photo online. Can you find out where it was taken?

The flag format is: csictf{latitude_longitude}
Example: csictf{40.7128_-74.0060}

Round to 4 decimal places.
```

- [location.jpg](./location.jpg)

## Exploit

This challenge requires you to identify the location where a photo was taken.

Steps:
1. Use reverse image search (Google Images, TinEye) to identify landmarks
2. Look for distinctive features in the image:
   - Architecture style
   - Signs or text in the image
   - Natural landmarks
   - Street signs or business names

3. Cross-reference with Google Maps or Google Earth

For this challenge, the image shows the Eiffel Tower in Paris, France.

Using Google Maps, you can find the exact coordinates of the Eiffel Tower:
- Latitude: 48.8584
- Longitude: 2.2945

The flag is:

```
csictf{48.8584_2.2945}
```
