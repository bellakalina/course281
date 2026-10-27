import numpy as np
import scipy
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt

 
def main():
    print("Python environment is working")
    print("numpy:", np.__version__)
    print("scipy:", scipy.__version__)
    print("matplotlib:", matplotlib.__version__)
    print("pandas:", pd.__version__)

    x = np.linspace(0, 2 * np.pi, 201)
    y = np.sin(x)

    data = pd.DataFrame({"x": x, "sin_x": y})

    assert len(data) == 201
    assert np.isclose(data["sin_x"].iloc[0], 0.0)

    plt.figure()
    plt.plot(x, y, label="sin(x)")
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    plt.title("Physics 281 Smoke Test")
    plt.legend()
    plt.tight_layout()
    plt.savefig("smoke_test_plot.png", dpi=150)
    plt.close()

    print("Saved smoke_test_plot.png")
    print("Smoke test completed successfully")


if __name__ == "__main__":
    main()
