from articles_data import db, Article
from app import app
from datetime import datetime
import re

# Function to create slug from title
def slugify(title):
    slug = re.sub(r'[^\w\s-]', '', title).strip().lower()
    slug = re.sub(r'[-\s]+', '-', slug)
    return slug

articles_data = [
    {
        'title': 'Unlocking Growth: Applying the 10 Types of Innovation Across Industries',
        'tag': 'INNOVATION',
        'summary': 'The Ten Types of Innovation framework by Doblin offers a holistic approach to innovation by identifying ten areas where companies can differentiate and create value—not just through products, but also through processes, business models, customer engagement, and more.',
        'image': 'images/home/articles/article_1_people_brainstorming.jpg',
        'author': 'Mauricio Aragon',
        'published_on': datetime(2025, 5, 1),
        'content': '''
            <p>In a world where innovation is often equated with flashy tech or sleek design, many organizations overlook the broader range of ways they can stand out and create value. 
            This is where Doblin's Ten Types of Innovation framework proves invaluable. Developed by the Doblin Group (now part of Deloitte), this model provides a comprehensive lens through which companies can assess and improve their innovation strategies—not just in products, but across their entire business model.
            Rather than focusing solely on product innovation, the framework categorizes innovation into three broad areas: Configuration, Offering, and Experience—with ten specific types across those categories.</p>

            <h2>Why ABM is Essential for Modern Companies</h2>
            <h3>1. Precision Targeting</h3>
            <p>ABM begins with identifying key accounts — the companies that most closely align with your ideal customer profile. 
            This ensures that marketing efforts aren't wasted on low-value prospects, and that teams focus on building campaigns that resonate with stakeholders who actually have the buying power.</p>

            <h3>2. Marketing and Sales Alignment</h3>
            <p>One of the greatest strengths of ABM is how it forces collaboration between sales and marketing. 
            Teams work together to identify target accounts, define goals, and execute tailored outreach plans.
            This unity ensures messaging is consistent, strategic, and relevant throughout the entire customer journey.</p>

            <blockquote>
                “Innovation is rarely about a single breakthrough — it's a strategic system of approaches that work together.”
            </blockquote>

            <p>By understanding and applying multiple types of innovation, companies can build defensible strategies that outperform their competition.</p>
        '''
    },
    {
        'title': '10 Best AI Tools for Creative Work',
        'tag': 'TECHNOLOGY',
        'summary': 'Artificial intelligence is rapidly transforming the way creative professionals work—boosting productivity, expanding artistic possibilities, and removing tedious tasks from the process.',
        'image': 'images/home/articles/article_3_AI_Tools.jpg',
        'author': 'Mauricio Aragon',
        'published_on': datetime(2025, 5, 1),
        'content': '''
            <p>Artificial intelligence is rapidly transforming the way creative professionals work—boosting productivity, expanding artistic possibilities, and removing tedious tasks from the process. 
            From generating visuals to enhancing writing and editing workflows, today's AI tools can help designers, writers, and creators take their projects to new levels.</p>

            <h2>My Top Picks</h2>

            <h3>1. Adobe Firefly</h3>
            <p>A powerful generative AI tool built into Adobe's Creative Cloud suite. It allows creators to generate images, vectors, and design elements from simple text prompts.</p>

            <h3>2. Runway</h3>
            <p>Runway offers a suite of AI-powered video and image editing tools, ideal for content creators, filmmakers, and designers looking to experiment with generative media.</p>

            <h3>3. ChatGPT</h3>
            <p>Great for brainstorming ideas, generating copy, rewriting drafts, or even assisting with creative coding for interactive experiences.</p>

            <h3>4. Midjourney</h3>
            <p>An AI image-generation tool that produces highly artistic and imaginative visuals based on textual prompts—popular with designers and illustrators.</p>

            <h3>5. Descript</h3>
            <p>A collaborative audio/video editing platform that uses AI to simplify transcription, editing, and voice cloning—perfect for podcasters and video editors.</p>

            <h3>6. Canva Magic Studio</h3>
            <p>Canva's AI suite includes text-to-image generation, Magic Write (AI writing assistant), and layout suggestions to speed up design tasks for marketers and content teams.</p>

            <h3>7. DALL·E</h3>
            <p>Created by OpenAI, DALL·E can generate unique and often surreal images from prompts—ideal for conceptual art, mood boards, and experimental design work.</p>

            <h3>8. Notion AI</h3>
            <p>Helps creatives organize, generate, and improve content inside the Notion workspace. Great for planning, ideating, or generating rough drafts of blog posts or strategies.</p>

            <h3>9. GrammarlyGO</h3>
            <p>Goes beyond grammar correction to offer real-time writing suggestions powered by AI. Tailor tone, clarity, and intent for different content types.</p>

            <h3>10. Figma AI</h3>
            <p>Figma has begun integrating AI features that suggest design components, automate repetitive tasks, and accelerate UI/UX workflows.</p>

            <blockquote>
                “AI won't replace creativity—it will supercharge it, freeing people to focus on what humans do best: imagine, design, and innovate.”
            </blockquote>

            <p>As creative work evolves, integrating the right AI tools can enhance not just what we make—but how we think about making it. Whether you're a solo creator or part of a larger team, experimenting with these tools can unlock new levels of efficiency and inspiration.</p>
        '''
    },
    {
        'title': 'Account Based Marketing: Time for a Strategic Approach',
        'tag': 'MARKETING STRATEGY',
        'summary': 'Account Based Marketing (ABM) has evolved from a buzzword to a strategic pillar in modern B2B marketing. It offers a focused, efficient approach to engage high-value accounts with precision.',
        'image': 'images/home/articles/article_2_people_office.jpg',
        'author': 'Mauricio Aragon',
        'published_on': datetime(2025, 5, 1),
        'content': '''
            <p>Account Based Marketing (ABM) has evolved from a buzzword to a strategic pillar in modern B2B marketing. 
            As organizations seek greater ROI, more meaningful customer relationships, and alignment between sales and marketing, ABM offers a focused, efficient approach to engage high-value accounts with precision.</p>

            <h2>Why ABM Is More Relevant Than Ever</h2>

            <h3>1. Targeted Efficiency</h3>
            <p>ABM enables teams to concentrate resources on high-potential accounts. Rather than casting a wide net, marketers identify and prioritize companies most likely to convert—maximizing relevance and minimizing waste.</p>

            <h3>2. Sales and Marketing Alignment</h3>
            <p>ABM fosters tight collaboration between sales and marketing. These teams co-develop campaigns tailored to specific accounts, ensuring messaging is consistent and highly personalized across all touchpoints.</p>

            <h3>3. Personalization at Scale</h3>
            <p>With the help of data and automation, ABM allows for deep personalization across selected accounts—without requiring manual effort for each interaction. This leads to stronger engagement and better outcomes.</p>

            <h3>4. Better ROI Tracking</h3>
            <p>ABM simplifies measurement by focusing on defined targets. Teams can clearly track engagement, pipeline influence, and revenue tied to specific accounts, making it easier to justify marketing spend.</p>

            <h3>5. Long-Term Relationship Building</h3>
            <p>ABM is not about quick wins. It's a long-term strategy built on trust, relevance, and value. Successful ABM programs often result in deeper partnerships and higher customer lifetime value.</p>

            <blockquote>
                “ABM isn't a tactic—it's a shift in mindset that puts relationships and relevance at the center of B2B marketing.”
            </blockquote>

            <p>As buyer journeys become more complex and decision-making teams expand, adopting a strategic ABM approach can help organizations cut through the noise, speak directly to what matters, and drive sustainable growth.</p>
        '''
    }
]

with app.app_context():
    for data in articles_data:
        slug = slugify(data['title'])
        existing = Article.query.filter_by(slug=slug).first()
        if not existing:
            a = Article(
                title=data['title'],
                slug=slug,
                tag=data['tag'],
                summary=data['summary'],
                image=data['image'],
                author=data['author'],
                published_on=data['published_on'],
                content=data['content']
            )
            db.session.add(a)
            print(f" Added: {data['title']}")
        else:
            print(f" Skipped (already exists): {data['title']}")
    db.session.commit()
    print("Done")