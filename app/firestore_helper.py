from firebase_admin import firestore

COLLECTION_NAME = 'score-board'
DOCUMENT_NAME = 'board1'


# Following function is used for initializing database for the first time
def initializeScoreboard(db):
    print("Initializing the board")
    doc_ref = db.collection(COLLECTION_NAME)
    day1 = {'away': int(0),
            'home': int(0) }
    doc_ref.document(DOCUMENT_NAME).set(day1)


# Following function is used for getting the score in case db is initialized, else initialize db and return score
def getGoal(db):
    doc_ref = db.collection(COLLECTION_NAME).document(DOCUMENT_NAME)
    board = doc_ref.get().to_dict()
    if(board):
        board['home'] = int(board['home'])
        board['away'] = int(board['away'])
        return(board)  
    else:
        print("No such board exists, creating a board")
        initializeScoreboard(db)
        return({'away': int(0), 'home': int(0) })           



# Following function is used for updating scoreboard, incase db is not initailized, initialize db and return score
def updateScoreBoard(db,team):
    # [START update_data_transaction_result]
    transaction = db.transaction()
    doc_ref = db.collection(COLLECTION_NAME).document(DOCUMENT_NAME)
    board = doc_ref.get().to_dict()
    if board:
        @firestore.transactional
        def update_in_transaction(transaction, doc_ref, team):
            snapshot = doc_ref.get(transaction=transaction).to_dict()
            print("Before updating: " + str(snapshot))
            snapshot[team] = snapshot.get(team) + 1
            transaction.update(doc_ref, snapshot)
            print("After updating: " + str(snapshot))
            return snapshot
        score = update_in_transaction(transaction, doc_ref, team)
        return score
    else:
        print("No such board exists, creating a board")
        initializeScoreboard(db)
        return updateScoreBoard(db,team)
    # [END update_data_transaction_result]
