def ModelPerformance():

    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    m = 0.4
    c = 2.4

    Y_pred = []

    print("Predicted Y values:")

    for x in X:
        y = m * x + c
        Y_pred.append(y)
        print("X =", x, " Predicted Y =", round(y,2))

    # -------- MSE --------
    print("\nCalculating MSE")

    n = len(Y)
    mse_sum = 0

    for i in range(n):
        error = Y[i] - Y_pred[i]
        sq_error = error ** 2

        print("Actual:",Y[i]," Predicted:",round(Y_pred[i],2)," Error^2:",round(sq_error,2))

        mse_sum += sq_error

    MSE = mse_sum / n

    print("\nMean Squared Error =", round(MSE,2))

    # -------- R2 Score --------
    print("\nCalculating R2 Score")

    mean_y = sum(Y) / n

    ss_total = 0
    ss_res = 0

    for i in range(n):
        ss_total += (Y[i] - mean_y) ** 2
        ss_res += (Y[i] - Y_pred[i]) ** 2

    r2 = 1 - (ss_res / ss_total)

    print("R2 Score =", round(r2,2))


def main():
    ModelPerformance()


if __name__ == "__main__":
    main()