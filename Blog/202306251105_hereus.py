from Blog.Super import Super
from datetime import datetime
import os

data = {
    'id': os.path.basename(__file__).split('_')[1].removesuffix('.py'),
    'title': 'Reflecting on HereUS: A Year of Growth and Innovation',
    'content': '''
<h2>Introduction:</h2>
<p><p>One year ago, on June 25, 2022, we launched HereUS with the vision of creating a safe and secure platform for people of all backgrounds. Today, we take pride in achieving this goal through immense effort and dedication. However, significant changes have taken place. In our upcoming update, users will need to choose a client to access HereUS. Rest assured, our team will continue to provide a client directly developed by us. We are thrilled to announce the HereUS Client, but if you prefer an alternative, we are also verifying third-party clients, ensuring a reliable and trustworthy experience. Over the next year, we will introduce new HereUS clients that cater to different user types. But before we look ahead, let's take a moment to reflect on the journey of HereUS 1 and HereUS 2.</p></p>



<h2>HereUS 1: The Early Milestones (Released: June 2022)</h2>

<h3>One year ago, we released the initial version of HereUS, packed with the following features:</h3>
<p>1. A feed that regenerates with posts exclusively from accounts you follow.</p>
<p>2. Easy-to-discover communities.</p>
<p>3. Fast and private chat feature.</p>
<p>4. Profile pages with display names and unlimited status texts.</p>

<h3>Just six days later, we released the "July 2022, 1.0.1" update, expanding the platform's capabilities:</h3>
<p>1. Expanded view for posts.</p>
<p>2. Commenting on posts.</p>
<p>3. Ability to use HTML in posts.</p>
<p>4. Introduction of sub-communities.</p>
<p>5. Announcements page for communities.</p>
<p>August 2022, 1.0.2: </p>

<h3>Continuing our rapid development, just a month later, we unveiled the "August 2022, 1.0.2" update, which introduced exciting new features:</h3>
<p>1. Enhanced discoverability for communities.</p>
<p>2. Styleable and picture attachable comments.</p>
<p>3. Follower count visibility for accounts.</p>
<p>4. Cross-posting functionality.</p>
<p>5. Ability to remove comments.</p>
<p>6. Mobile apps for HereUS.</p>



<h2>HereUS 2: Expanding Horizons (Released: September 2022)</h2>

<h3>Within the first three months of HereUS, we unveiled HereUS 2, enriching the user experience with the following features:</h3>
<p>1. The Explore Feed, broadening your content discovery.</p>
<p>2. Rules pages for communities, ensuring a healthy and respectful environment.</p>
<p>3. Special sub-community type with Chat UI, fostering real-time engagement.</p>
<p>4. HereUS Articles, offering a platform for sharing long-form content.</p>
<p>5. Modernized UI, enhancing visual appeal and usability.</p>
<p>6. Dark Mode, for those who prefer a darker interface.</p>
<p>7. Ability to add biography text to profile pages.</p>
<p>8. Color palette customization, allowing users to personalize their experience.</p>
<p>9. Expandable post texts, providing room for more content.</p>
<p>10. Ability to write longer posts in a single entry.</p>
<p>11. Events page for communities, facilitating event management.</p>
<p>12. About view for communities, enabling concise information sharing.</p>

<h3>As autumn arrived, we released the "Autumn 2022, 2.0.1" update, which introduced further enhancements:</h3>
<p>1. Create chat directly from the profile page, simplifying communication.</p>
<p>2. Support for additional languages, broadening accessibility.</p>
<p>3. Improved error pages, reducing the likelihood of encountering errors.</p>
<p>4. Easier login with "IP-Login," streamlining the authentication process.</p>
<p>5. Mobile compatibility for the HereUS website, enabling on-the-go access.</p>
<p>6. Community styling options, empowering community owners to customize their spaces.</p>
<p>7. Profile badges, recognizing achievements and contributions.</p>
<p>8. Introduction of HereUS Tokens, enhancing user rewards and benefits.</p>
<p>9. HereUS Plus, a premium offering with exclusive features.</p>
<p>10. HereUS Ads, providing opportunities for targeted advertising.</p>
<p>11. Exclusive themes (Silver, Cyan, Diamond), offering unique visual experiences.</p>

<h3>As HereUS entered its eighth month, the "Winter 2023, 2.0.2" update was released, focusing on ensuring long-term viability:</h3>
<p>1. Beta channel for HereUS, enabling users to experience upcoming features.</p>
<p>2. Color scheme guide, facilitating user customization.</p>
<p>3. Introducing "HereUS Sohbet" a new chat app compatible with ASD Protocol.</p>
<p>4. "Do not recommend" button, allowing users to fine-tune their recommendations.</p>
<p>5. Addition of the Tokyo theme, expanding visual choices.</p>
<p>6. Support for two more languages: German and Japanese.</p>

<h3>In the most recent update, "Spring 2023, 2.0.3" HereUS introduced exciting features that captivated users:</h3>
<p>1. App Status, providing real-time information on the platform's availability.</p>
<p>2. ASDG support for "HereUS Sohbet," further enhancing accessibility.</p>
<p>3. Ability to view the list of followers, fostering engagement and connection.</p>
<p>4. Profile pictures, enabling users to personalize their profiles.</p>
<p>5. Stories, a dynamic and ephemeral way of sharing content.</p>
<p>6. Introduction of the Forest theme, bringing a refreshing natural aesthetic.</p>
<p>7. Support for two additional languages: French and Korean.</p>



<h2>Introducing HereUS 3: The Next Chapter Begins</h2>

<h3>Now, we proudly introduce "HereUS 3," an exciting new phase for our platform. Here are the latest features it brings:</h3>
<p>A fresh UI, offering an enhanced and modern look.</p>
<p>Bars Accounts for HereUS, providing additional options for user management.</p>
<p>Ability to search for HereUS results within Bars, ensuring seamless exploration.</p>
<p>Poke the Nostalgia Feature, evoking fond memories through interactive experiences.</p>
<p>Introduction of the Amethyst theme, adding a touch of elegance and allure.</p>

<p>Alongside HereUS 3, we are replacing HereUS Tokens with Bars Tokens and HereUS Plus with Bars Plus. These changes mark our commitment to continual growth and improvement. Thank you for being an essential part of the HereUS community.</p>
    ''',
    'datetime': datetime.strptime(os.path.basename(__file__).split('_')[0].split('/')[-1], '%Y%m%d%H%M')
}


get = Super(data).get
