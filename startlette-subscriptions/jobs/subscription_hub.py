from collections import defaultdict
from asyncio import Queue


class SubscriptionHub:
    def __init__(self):
        self.subscriptions = defaultdict(list)

    def subscribe_to_job(self, job_id):
        queue = Queue()

        self.subscriptions[job_id].append(queue)

        return queue

    def update_job(self, job_id, job):
        # No one is listening to the this job
        if job_id not in self.subscriptions:
            return

        queues = self.subscriptions[job_id]
        for queue in queues:
            queue.put_nowait(job)

    def unsubscribe(self, job_id, queue):
        queues = self.subscriptions[job_id]
        queues.remove(queue)


hub = SubscriptionHub()
