# Priority Queue

**Problem:**  
Implement a simple priority queue. Assume an incoming stream of dictionaries containing two keys; command to be executed and priority. Priority is an integer value [0, 10], where work items of the same priority are processed in the order they are received.

**Solution:**  
Priority Queue implemented in `priority_queue.py` as a `Binary Max Heap`.

**Usage:**
Import and instantiate `priority_queue`:

```
pq = PriorityQueue()
```

Add list of nodes (dict) containing the `priority` value and `command` function:

```
nodes = [
    {'priority': 1, 'command': <function>},
    {'priority': 10, 'command': <function>},
    {'priority': 5, 'command': <function>},
]
pq.insert_nodes(nodes)
```

Alternatively, you can add a single node:

```
node = {'priority': 5, 'command': <function>}
pq.insert_node(nodes)
```

Pop the highest priority node:

```
node = pq.pop_priority_node()
print(node)
>> {'priority': 10, 'command': <function>}
```

Or pop highest priority node and execute command:

```
pq.exec_next_command()
```

# Questions

### 1. Please explain Big-O notation in simple terms.

The number of steps needed to solve a problem, which can grow depending on the size of the input (n) you give to the problem. It is used to analyze an algorithms worst-case performance. The O notation is an indication of the growth, and not of the actual performance. For example, when searching for duplicated values in an unsorted list, our algorithm might do n^2 operation, because for every item of n items we search through the full list again to make a comparison, resulting in O(n^2). If we increase n, the growth is exponential. For growth, 100n^2 is the same as n^2, thus we can hide leading constants to make for a hardware independent analysis. We might adjust by sorting the list first, which can improve the algorithm to O(nlogn), which means increasing the input would cause a slower growth than it would for an exponential algorithm.

### 2. What are the most important things to look for when reviewing another team member's code?

- Check if code solves the initially defined problem, and if it could potentially cause other issues.
- Check if the code is legible and intuitive without having to read comments and documentation. If not, check if documention exits.
- Check if code follows DRY, low coupling, and high cohesion princicples.
- Check if code follows the style guide of the programming language (ex: PEP 8).
- Check how code handles errors and exceptions, and if there is sufficient logging.
- Check security of code. Ex) Is the author commiting important API keys?
- Check if merge request has details about the problem and how the code solves those problems.

### 3. Describe a recent interaction with someone who was non-technical. What did you need to communicate and how did you do it?

I had a recent interaction with someone who wasn't receiving emails with attachments in their Outlook. Removing technical jargon and using an analogy I explained:

"Sending an email is like sending an envelope with a letter. That envelope with a single paged letter takes up a relatively small amount of space. An envelope with lots of photos takes up even more space.

That envelope is sent from the sender to the postal service and put in a box. Anything put in that box is automatically sent to you, but that box has limited space. If that box is almost full, it might only fit envelope with a single letter instead of one with lots of photos. If the mail is too big to fit, then it's not stored in the box and not sent to you.

You should call the internet company and ask them to check if your box is full." This made enough sense for them to call their ISP and immediately resolve the issue.
