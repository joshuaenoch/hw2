# provides methods to guage metric evaluations of model
# each method calculates how many predicted positives were correct
class MetricEvaluation:
    # define constuctor for metric object
    # initialize true values (y_true)
    # initialize predicted values (y_pred)
    def __init__(self, y_true, y_pred):
        self.y_true = y_true
        self.y_pred = y_pred

    # detmerine accuracy of predictions
    def accuracy_score(self):
        pred_counter = 0
        tot_preds = len(self.y_true)

        for i in range(tot_preds):
            # check if true value matches predicted value
            if self.y_true[i] == self.y_pred[i]:
                pred_counter += 1
        # determine accuracy as percent out of 100
        final_score = round((pred_counter/tot_preds) * 100)

        return final_score

    # determine precision of predictions
    def precision_score(self):
        prec = 0
        true_pos = 0
        false_pos = 0

        for i in range(len(self.y_true)):
            # test for true positive cases
            if self.y_true[i] == 1 and self.y_pred[i] == 1:
                true_pos += 1
            # test for false positive cases
            elif self.y_true[i] == 0 and self.y_pred[i] == 1:
                false_pos += 1

        # check if positive cases exist
        if true_pos + false_pos > 0:
            # use precision forumla to check number of correct predicted positives
            # calculate number as percent out of 100
            prec = round((true_pos / (true_pos + false_pos)) * 100)
        else:
            prec = 0

        return prec

    # determine recall of predictions
    def recall_score(self):
        rec = 0
        true_pos = 0
        false_neg = 0

        for i in range(len(self.y_true)):
            # test for true positive cases
            if self.y_true[i] == 1 and self.y_pred[i] == 1:
                true_pos += 1
            # test for false negative cases
            elif self.y_true[i] == 1 and self.y_pred[i] == 0:
                false_neg += 1

        # check if positive cases exist
        if true_pos + false_neg > 0:
            # use recall forumla to check number of correct predicted positives
            # calculate number as percent out of 100
            rec = round((true_pos / (true_pos + false_neg)) * 100)
        else:
            rec = 0

        return rec

    def f1_score(self):
        f1 = 0
        # call precision method to aquire score
        prec = self.precision_score()
        # call recall method to acquire score
        rec = self.recall_score()

        if prec + rec > 0:
            # use F1 formula to measure model's accuracy 
            f1 = round((2 * prec * rec) / (prec + rec))
        else:
            f1 = 0
        
        return f1