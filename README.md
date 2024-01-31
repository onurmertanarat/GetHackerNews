<h1>Get Hacker News</h1>

<p>Get Hacker News is a project that retrieves trending news from Hacker News using Python.</p>

<h2>Files</h2>

<p>The project includes three Python scripts:</p>

<ul>
    <li><strong>wo_gui.py:</strong> Python script that retrieves and prints trending news from Hacker News without a graphical user interface (GUI).</li>
    <li><strong>with_gui.py:</strong> Python script that retrieves and displays trending news from Hacker News with a GUI using Tkinter.</li>
    <li><strong>with_gui_threading.py:</strong> Python script that retrieves and displays trending news from Hacker News with a GUI using Tkinter and threading for better performance.</li>
</ul>

<h2>Usage</h2>

<ol>
    <li>To run <code>wo_gui.py</code>, execute the following command in your terminal:</li>
    <pre><code>python wo_gui.py</code></pre>
    <li>To run <code>with_gui.py</code>, execute the following command in your terminal:</li>
    <pre><code>python with_gui.py</code></pre>
    <li>To run <code>with_gui_threading.py</code>, execute the following command in your terminal:</li>
    <pre><code>python with_gui_threading.py</code></pre>
</ol>

<h2>Threading Usage</h2>

<p>The <code>with_gui_threading.py</code> script utilizes threading to improve performance when retrieving and displaying news from Hacker News. Threading allows the GUI to remain responsive while the news data is being fetched in the background. This ensures a smoother user experience, especially when dealing with potentially slow network requests.</p>

<p>By using threading, the main GUI thread is not blocked by the network request, allowing the user to interact with the interface without experiencing delays or freezes. As a result, the application feels more responsive and efficient.</p>

<h2>Contributing</h2>

<p>If you would like to contribute, please open an issue or submit a pull request. Your constructive contributions are welcome!</p>
