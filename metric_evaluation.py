import pandas as pd

class MetricEvaluation:
    def __init__(self, y_true, y_pred):
       
        self.y_true = y_true
        self.y_pred = y_pred

    def accuracy_score(self):
        pred_counter = 0
        tot_preds = len(self.y_true)
        for i in range(tot_preds):
            if self.y_true[i] == self.y_pred[i]:
                pred_counter += 1
        final_score = round((pred_counter/tot_preds) * 100)
        return final_score

    def precision_score(self):
        prec = 0
        true_pos = 0
        false_pos = 0

        for i in range(len(self.y_true)):
            if self.y_true[i] == 1 and self.y_pred[i] == 1:
                true_pos += 1
            elif self.y_true[i] == 0 and self.y_pred[i] == 1:
                false_pos += 1

        if true_pos + false_pos > 0:
            prec = round((true_pos / (true_pos + false_pos)) * 100)
        else:
            prec = 0

        return prec

    def recall_score(self):
        rec = 0
        true_pos = 0
        false_neg = 0

        for i in range(len(self.y_true)):
            if self.y_true[i] == 1 and self.y_pred[i] == 1:
                true_pos += 1
            elif self.y_true[i] == 1 and self.y_pred[i] == 0:
                false_neg += 1

        if true_pos + false_neg > 0:
            rec = round((true_pos / (true_pos + false_neg)) * 100)
        else:
            rec = 0

        return rec

    def f1_score(self):
        f1 = 0
        prec = self.precision_score()
        rec = self.recall_score()

        if prec + rec > 0:
            f1 = round((2 * prec * rec) / (prec + rec))
        else:
            f1 = 0
        
        return f1