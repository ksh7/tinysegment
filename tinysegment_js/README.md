# Tiny Segment App

### Instructions
- Add tinysegment.js library in your website where you've configured twilio segment.

- Configure it by adding values like including element ids that needs to trigger code updates:
```
                // Initialize TinySegment.js

                tinySegmentAPIURL.initializeAPIUrl('https://tiny.aenv.site/api_fetch_code');
                
                tinySegmentScrollObserver.initializeElments(["heading_banner_page1", "pricing_details_page1", "article_description_page1"]);
                
                tinySegmentElementTracking.initializeEvents([{"heading_banner_page1": "viewing_header"}, {"pricing_details_page1": "viewing_pricing"}, {"article_description_page1": "viewing_article"}]);
   ```

- For above elements ids and events create respective code components and conditions in web app

- Now you can start viewing parts of your website being update based on who is visiting your pages.