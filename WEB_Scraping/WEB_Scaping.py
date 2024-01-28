import requests
from bs4 import BeautifulSoup
import tkinter as tk

def scrape_google_search(query):
    try:
        url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            search_results = soup.find_all('div', class_='tF2Cxc')

            if search_results:
                result_text = ""
                for result in search_results:
                    title = result.find('h3').text
                    snippet_element = result.find('span', class_='aCOpRe')

                    if snippet_element is None:
                        snippet_element = result.find('span', class_='hgKElc')

                    snippet = snippet_element.text if snippet_element else "Snippet not available"
                    link = result.find('a')['href']

                    # Include a unique tag for styling and linking
                    result_text += f"<title>{title}</title>\n<snippet>{snippet}</snippet>\n" \
                                f"<link href='{link}'>{link}</link><br><br>\n" \
                                f"--------------------------------------------\n"

                display_results(result_text)
            else:
                display_results("No search results found.")
        else:
            display_results("Failed to fetch search results.")
    except requests.exceptions.ConnectionError as e:
        print("Network not connected")  # Print to console for debugging
        display_results("", network_error=True)  # Pass network error flag to display_results

def display_results(results_text, network_error=False):
    if network_error:
        results_text_widget.delete("1.0", tk.END)
        results_text_widget.insert(tk.END, "Network not connected. Please check your internet connection and try again.", "left")
    else:
        results_text_widget.delete("1.0", tk.END)
        results_text_widget.insert(tk.END, results_text)

        # Style titles and snippets (without link functionality)
        results_text_widget.tag_config("title", foreground="blue", font="bold")
        results_text_widget.tag_config("snippet", font="italic")

root = tk.Tk()
root.title(" Web Scraping Tool ")
root.geometry("700x600")

main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

canvas = tk.Canvas(main_frame)
scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

canvas.create_window((0,0), window=scrollable_frame, anchor="nw")

canvas.pack(side="left", fill=tk.BOTH, expand=True)
scrollbar.pack(side="right", fill="y")

search_box = tk.Entry(scrollable_frame, width=40, font=("Arial", 14))
search_box.pack(pady=15, ipady=5, ipadx=10)
search_box.config(justify="center", relief="groove")  # Rounded corners for search box

search_button = tk.Button(scrollable_frame, text="Search ", font=("Cambria", 12), command=lambda: scrape_google_search(search_box.get()))
search_button.pack(pady=5)

results_text_widget = tk.Text(scrollable_frame, wrap=tk.WORD)
results_text_widget.tag_configure("left", justify="left")
results_text_widget.insert("1.0", " ", "left")  # Force left alignment
results_text_widget.pack(pady=15, padx=10, fill=tk.BOTH, expand=True)

root.mainloop()
