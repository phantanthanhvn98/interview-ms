'''
1. Spots Trade:
    I don't know how to check the buy price when they sell and having many buy transactions bu this coin before. I propose we can make a average price. They buy 0.1 $BTC at 20k$, 0,1 $BTC at 30k$. Now the average price is 25k$
    We can use the average price to cacl when they sell
2. Scalibility:
    I can design:
    1. Crawl service: the purpose of this service is we can crawl all transactions of our clients and store it to database with field processed = False
        cron job will sync transations from exchanges is real time and store to database only. ONLY STORE
    2. The clean service: cacl avarage price or cacl teh future posotion for each clients -> processed = True
        cron job to do it every a mount of time and change the row to processed = True
    3. Report service: we can use table form clean service and make the report -> We get a sell transaction so we use this service to calc the gain/loss and store to report_table
    4. Notification service with consumer kafka -> open websocket to notify events to FE
    5. master service: use for sign in, sign up, .....
'''