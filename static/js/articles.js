const articles = [
  {
    image: "images/home/articles/article_3_AI_Tools.jpg",
    tag: "TECHNOLOGY",
    title: "10 Best AI tools for creative work",
    summary: "AI is redefining how professionals across departments think, plan, and execute creative work. Get to know some of the most innovative AI-powered tools that support creativity, strategic thinking, and productivity across marketing, HR, operations, sales, and more.",
    link: "articles/article-2.html"
  },
   {
    image: "images/home/articles/article_2_people_office.jpg",
    tag: "STRATEGY",
    title: "Account Based Marketing: Time for a strategic approach",
    summary: "Account-Based Marketing (ABM) flips the traditional marketing funnel by focusing on high-value accounts instead of individual leads. This article explores how ABM aligns marketing and sales for targeted growth, builds stronger relationships, and leverages CRM systems to personalize campaigns at scale.",
    link: "articles/article-3.html"
  },

    {
    image: "images/home/articles/article_1_people_brainstorming.jpg",
    tag: "INNOVATION",
    title: "Unlocking Growth: Applying the 10 Types of Innovation Across Industries",
    summary: "The Ten Types of Innovation framework by Doblin offers a holistic approach to innovation by identifying ten areas where companies can differentiate and create value—not just through products, but also through processes, business models, customer engagement, and more.",
    link: "articles/article-1.html"
  }
];

// Generating a full list on the articles page
const fullGrid = document.getElementById("articlesGrid");
if (fullGrid) {
  articles.forEach(article => {
    const card = createArticleCard(article);
    fullGrid.appendChild(card);
  });
}

// Selecting random articles for the homepage
const homepageGrid = document.getElementById("featuredArticles");
if (homepageGrid) {
  const random = getRandomArticles(articles, 3);
  random.forEach(article => {
    const card = createArticleCard(article);
    homepageGrid.appendChild(card);
  });
}

// Creating an article card 
function createArticleCard(article) {
  const card = document.createElement("div");
  card.className = "card";
  card.innerHTML = `
    <img src="${article.image}" alt="${article.title}" />
    <div class="card-content">
      <span class="tag">${article.tag}</span>
      <h3>${article.title}</h3>
      <p>${article.summary}</p>
      <a href="${article.link}" class="btn-small">Read</a>
    </div>
  `;
  return card;
}

// Pick random items
function getRandomArticles(arr, count) {
  const shuffled = [...arr].sort(() => 0.5 - Math.random());
  return shuffled.slice(0, count);
}