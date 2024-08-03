<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <div>
        <h1>🚀 Air University Merit List Scraper and Checker 🚀</h1>
        <p>Welcome to the <strong>Air University Merit List Scraper and Checker</strong> repository! 🕵️‍♂️✨ Dive into the digital underworld of academic merit with this high-octane web scraping tool and search interface. Perfect for those who want to keep an eye on their academic fate without the usual red tape. 📊💻</p>
        <h2>🛠️ What's Inside?</h2>
        <ul>
            <li><strong>Web Scraper</strong> 🕸️
                <ul>
                    <li><strong>Purpose:</strong> This covert operation extracts merit list data from Air University's hidden portals with surgical precision. Built to handle a massive number of requests concurrently, this script employs a mix of scraping techniques and multithreading to deliver results faster than a cheetah on caffeine. 🐆⚡</li>
                    <li><strong>Key Tools:</strong> Python, <code>requests</code>, <code>BeautifulSoup</code>, <code>pandas</code>, and <code>concurrent.futures</code>.</li>
                </ul>
            </li>
            <li><strong>Dataset</strong> 📁
                <ul>
                    <li><strong>Contents:</strong> A treasure trove of academic data, including admit card numbers, merit positions, full names, and program preferences. This is your golden key to unlocking the hidden realms of merit scores and more.</li>
                </ul>
            </li>
            </li>
        </ul>
        <h2>🧩 How It Works</h2>
        <h3>1. The Scraper</h3>
        <p><strong>Objective:</strong> Extracts detailed merit information from Air University's backend systems.</p>
        <p><strong>Mechanics:</strong></p>
        <ul>
            <li><strong>Initial Recon:</strong> Requests the form fields from the target URL to establish a connection.</li>
            <li><strong>Payload Generation:</strong> Dynamically crafts requests to fetch student results based on admit card numbers.</li>
            <li><strong>Concurrent Execution:</strong> Uses <code>ThreadPoolExecutor</code> to manage multiple requests simultaneously, ensuring swift data retrieval.</li>
        </ul>
        <h3>2. The Dataset</h3>
        <p><strong>Data Contents:</strong> 
            <ul>
                <li><code>Admit Card Number</code></li>
                <li><code>Full Name</code></li>
                <li><code>1st Preference</code></li>
                <li><code>Aggregate Merit Score</code></li>
            </ul>
        </p>
        <p><strong>Usage:</strong> Enables quick lookups of merit positions via the web checker.</p>
        <p><strong>Features:</strong></p>
        <ul>
            <li><strong>Search Interface:</strong> Users can enter admit card numbers or full names to retrieve their merit positions.</li>
            <li><strong>Design:</strong> Minimalist design with a focus on functionality. The interface is responsive and designed for quick data retrieval.</li>
        </ul>
        <h2>📜 Getting Started</h2>
        <h3>1. Clone the Repository</h3>
        <pre><code>git clone https://github.com/TBO22/AU_Merit_List_24.github.io
cd AU_Merit_List_24</code></pre>
        <h3>2. Set Up the Scraper</h3>
        <p><strong>Dependencies:</strong></p>
        <pre><code>pip install requests beautifulsoup4 pandas</code></pre>
        <p><strong>Run the Scraper:</strong></p>
        <p>Modify the <code>collect_merit_data()</code> parameters if needed, and execute the script:</p>
        <pre><code>python scraper.py</code></pre>
        <p>This will generate <code>merit_list.csv</code> with all the data you need.</p>
        <h2>🕵️‍♂️ The Code's Secret Sauce</h2>
        <p>The scraper is designed to handle high-load scenarios efficiently. Here's a peek into its core features:</p>
        <ul>
            <li><strong>ThreadPoolExecutor:</strong> Manages concurrent requests to avoid bottlenecks.</li>
            <li><strong>Dynamic Payload Construction:</strong> Adapts to the form requirements of the target portal.</li>
            <li><strong>Asynchronous Processing:</strong> Processes results as soon as they're available, optimizing performance.</li>
        </ul>
        <h2>🔐 Disclaimer</h2>
        <p>This tool is an independent project and is not officially affiliated with Air University. It’s intended for educational and personal use only. Handle with care and respect the privacy and terms of service of your data sources.</p>
        <h2>🤖 Contribute or Report Issues</h2>
        <p>Found a bug or have suggestions? Feel free to open an issue or submit a pull request. Let’s keep this tool sharp and effective.</p>
        <p><strong>Stay anonymous, stay curious, and may the code be ever in your favor.</strong> 👨‍💻🕶️💾</p>
    </div>
</body>
</html>
