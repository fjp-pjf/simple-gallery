from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate

app = FastAPI()

text_posts = {
    1: {
    "title": "Why JavaScript Feels Weird at First",
    "content":
      "JavaScript is flexible to a fault. Hoisting, coercion, and async behavior confuse beginners, but once you understand the execution model, it becomes predictable and powerful."
  },
  2: {
    "title": "Node.js Is Single-Threaded — So Why Is It Fast?",
    "content":
      "Node.js uses a single-threaded event loop but offloads heavy tasks to the thread pool. Non-blocking I/O is the real reason it scales well."
  },
  3: {
    "title": "POST vs PUT vs PATCH (Without the BS)",
    "content":
      "POST creates, PUT replaces the entire resource, PATCH updates partially. People misuse POST for updates because APIs are messy, not because the rule is wrong."
  },
  4: {
    "title": "React Performance Myths",
    "content":
      "useMemo and React.memo don’t magically make your app fast. They help only when re-renders are actually expensive. Measure before optimizing."
  },
  5: {
    "title": "Why MVC Still Matters",
    "content":
      "MVC enforces separation of concerns. Even if frameworks evolve, the idea of isolating data, logic, and UI is still solid engineering."
  },
  6: {
    "title": "Frontend Interviews Test Fundamentals, Not Frameworks",
    "content":
      "Good interviews focus on closures, async behavior, and state management. Frameworks change; fundamentals don’t."
  },
  7: {
    "title": "Side Projects Don’t Fail — People Quit",
    "content":
      "Most projects die due to loss of direction, not complexity. Define a small goal, ship it, then improve."
  }
}

@app.get("/posts")
def get_all_posts(limit: int = None):
    return list(text_posts.values())[:limit]

@app.get("/posts/{id}")
def get_post(id: int) -> PostCreate:
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(id)

@app.post("/posts")
def create_post(post: PostCreate) -> PostCreate:
    new_post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post
