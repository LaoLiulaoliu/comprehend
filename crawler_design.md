##Crawler Desin thinking

###Modular
1. Login
    * no login
    * interactive js login
    * captcha

2. Source url
    * seed url
    * dequeue

3. Download
    * html download
    * load js
    * cache webpage
    * download with captcha
    * throttling 
    * concurrent crawling

4. Queue
    * enqueue
    * dequeue
    * distributed

5. parse
    * xpath
    * cssselect

6. save
    * to json
    * asynchronous queue to DB
    * enqueue


###Programming class rule:
1. scenario flow: Login, (download|dequeue)，parse，(json|db|enqueue)

2. one class in one flow, one class can enqueue to second class.

3. Initial several queue, queue bound to class, class sequence.

4. schedule, start with first class. class two is begin after one or sleep several seconds after class one start.

5. error handler.
