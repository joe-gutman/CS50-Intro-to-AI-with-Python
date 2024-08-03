import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 5000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages

def probability_check(model):
    probability_check = 0
    for page in model:
        probability_check += model[page]

    if not (0.999 <= probability_check <= 1.001):
        return False
    return True


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    # MY SOLUTION
    model = {}
    link_count = len(corpus[page])
    page_count = len(corpus)

    page_probability = (1 - damping_factor) / page_count 

    if link_count > 0:
        link_probability = damping_factor / link_count
        for link in corpus[page]:
            if link != page:
                model[link] = link_probability
    else:
        link_probability = damping_factor / page_count
        for page in corpus:
            model[page] = link_probability

    for page in corpus:
        if page not in model:
            model[page] = page_probability
        else:
            model[page] += page_probability


    if probability_check(model):
        return model
    else:
        raise ValueError("Invalid probability distribution")
  


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    current_page = random.choice(list(corpus.keys()))
    page_visits = {}

    for _ in range(n):
        page_visits[current_page] = page_visits.get(current_page, 0) + 1
        model = transition_model(corpus, current_page, damping_factor)
        sorted_probabilities = []
        for page in model:
            if len(sorted_probabilities) > 0:
                for index, value in enumerate(sorted_probabilities):
                    if model[page] < model[value]:
                        sorted_probabilities.insert(index, page)
                        break
                if page not in sorted_probabilities: 
                    sorted_probabilities.append(page)
            else: 
                sorted_probabilities.append(page) 

        cumulative_probabilities = {}
        cumulative_sum = 0
        for page in sorted_probabilities:
            cumulative_sum += model[page]
            cumulative_probabilities[page] = cumulative_sum

        random_value = random.random()
        for page in cumulative_probabilities:
            if random_value < cumulative_probabilities[page]:
                current_page = page
                break     

    page_rank = {}
    for page in corpus:
        if page not in page_visits:
            page_rank[page] = 0
        else:
            page_rank[page] = page_visits[page]/n

    if probability_check(page_rank):
        return page_rank
    else:
        raise ValueError("Invalid probability distribution")
            
                 
def has_converged(old_ranks, new_ranks, convergence_delta):
    for page in old_ranks:
        if abs(old_ranks[page] - new_ranks[page]) > convergence_delta:
            return False
    return True

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    iterate_count = 0
    num_pages = len(corpus)

    page_ranks = {page : 1 / num_pages for page in corpus}
    convergence_limit = .001

    while True:
        new_page_ranks = {}

        for page in page_ranks:
            new_rank = (1 - damping_factor) / num_pages
            for possible_page in corpus:
                if page in corpus[possible_page]:
                    new_rank += damping_factor * (page_ranks[possible_page] / len(corpus[possible_page]))
                elif not corpus[possible_page]:
                    new_rank += damping_factor * (page_ranks[possible_page] / num_pages)

            new_page_ranks[page] = new_rank

        if has_converged(page_ranks, new_page_ranks, convergence_limit):
            print(f"Converged after {iterate_count} iterations")
            if probability_check(new_page_ranks):
                return new_page_ranks
            else:
                raise ValueError("Invalid probability distribution")

        
        page_ranks = new_page_ranks
        iterate_count += 1
        

if __name__ == "__main__":
    main()
