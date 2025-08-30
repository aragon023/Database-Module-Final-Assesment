const tools = [
  {
    title: 'Empathy Map',
    image: '/static/images/tools/empathy_mapping.jpg',
    tags: ['Empathy'],
    description: 'Understand and articulate what a user experiences.',
    details: 'An Empathy Map is a simple, powerful tool used in design thinking and user-centered design. It captures insights about user behavior, emotions, and motivations. Typically divided into Think & Feel, Hear, See, Say & Do, Pains, and Gains, it is widely used early in product development.'
  },
  {
    title: 'Affinity Diagramming',
    image: '/static/images/tools/affinity_diagram.jpg',
    tags: ['Planning'],
    description: 'Group ideas into clusters to find patterns.',
    details: 'Affinity diagramming helps organize ideas, data, and insights by grouping them into meaningful categories or clusters. Its used to uncover relationships between concepts and is especially useful during brainstorming or synthesis phases.'
  },
  {
    title: 'Five Whys',
    image: '/static/images/tools/five_whys.jpg',
    tags: ['Problem Solving'],
    description: 'Explore root causes by asking "why" repeatedly.',
    details: 'The 5 Whys technique is a problem-solving method used to identify the root cause of a problem. By asking "Why?" five times (or more), you uncover deeper insights that help guide corrective action.'
  },
];

const grid = document.getElementById('toolGrid');

function renderCards(filter = 'All') {
  grid.innerHTML = '';
  tools.forEach(tool => {
    if (filter === 'All' || tool.tags.includes(filter)) {
      const card = document.createElement('div');
      card.className = 'card';
      card.innerHTML = `
        <img src="${tool.image}" alt="${tool.title}" />
        <h3>${tool.title}</h3>
        <p>${tool.description}</p>
        <div class="tags">${tool.tags.map(tag => `<span>${tag}</span>`).join(' ')}</div>
      `;
      card.addEventListener('click', () => showModal(tool));
      grid.appendChild(card);
    }
  });
}

function filterCards(tag) {
  renderCards(tag);
}

function showModal(tool) {
  document.getElementById('modalImage').src = tool.image;
  document.getElementById('modalTitle').innerText = tool.title;
  document.getElementById('modalDescription').innerText = tool.details || tool.description;
  document.getElementById('modalTags').innerHTML = tool.tags.map(tag => `<span>${tag}</span>`).join(' ');

  const modalExtra = document.getElementById('modalExtra');

  if (tool.title === 'Empathy Map') {
    modalExtra.innerHTML = `
      <div class="tool-steps">
        <h4>How to Use</h4>
        <ol>
          <li><strong>Define the User:</strong> Identify who you're mapping.</li>
          <li><strong>Set Up Quadrants:</strong> Says, Thinks, Does, Feels, Pains, Gains.</li>
          <li><strong>Fill the Map:</strong> Use sticky notes or digital input to capture insights.</li>
          <li><strong>Synthesize:</strong> Look for patterns or contradictions across quadrants.</li>
          <li><strong>Apply Insights:</strong> Use findings to guide design and strategy decisions.</li>
        </ol>
      </div>
    `;
  } else if (tool.title === 'Affinity Diagramming') {
    modalExtra.innerHTML = `
      <div class="tool-steps">
        <h4>How to Use</h4>
        <ol>
          <li><strong>Gather Ideas:</strong> Collect input from team discussions, interviews, or brainstorming.</li>
          <li><strong>Write Ideas:</strong> Record each idea on a sticky note or card.</li>
          <li><strong>Group Similar Ideas:</strong> Sort notes into clusters based on natural relationships.</li>
          <li><strong>Label Clusters:</strong> Name each group with a theme or insight.</li>
          <li><strong>Analyze:</strong> Review clusters to discover patterns and implications.</li>
        </ol>
      </div>
    `;
  } else if (tool.title === 'Five Whys') {
    modalExtra.innerHTML = `
      <div class="tool-steps">
        <h4>How to Use</h4>
        <ol>
          <li><strong>State the Problem:</strong> Clearly define the issue you are investigating.</li>
          <li><strong>Ask "Why?":</strong> Ask why the problem occurred.</li>
          <li><strong>Repeat:</strong> Continue asking "Why?" for each response (ideally 5 times).</li>
          <li><strong>Identify Root Cause:</strong> Stop when you uncover the fundamental reason.</li>
          <li><strong>Take Action:</strong> Develop a solution to address the root cause.</li>
        </ol>
      </div>
    `;
  } else {
    modalExtra.innerHTML = '';
  }

  document.getElementById('toolModal').style.display = 'block';
}

document.querySelector('.close-button').onclick = () => {
  document.getElementById('toolModal').style.display = 'none';
};

window.onclick = (event) => {
  if (event.target === document.getElementById('toolModal')) {
    document.getElementById('toolModal').style.display = 'none';
  }
};

renderCards();
