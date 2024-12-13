import calendar

from PySide6.QtWidgets import QDialog, QVBoxLayout, QComboBox
from PySide6.QtGui import QIcon, QPixmap
import data_base
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import arrow
import calendar

class Canvas(FigureCanvas):
    def __init__(self, width=22, height=10, dpi=100, parent=None):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)
        self.axes.plot()


class Graph(QDialog):
    def __init__(self, type, label):
        super().__init__()
        self.setWindowTitle("Графики")
        self.setWindowIcon(QPixmap("graph.png"))

        self.label = label
        self.type = type

        self.layout = QVBoxLayout()
        self.select_type = QComboBox()
        self.select_type.addItems(["По дням", "По месяцам", "По годам"])
        self.select_type.currentTextChanged.connect(self.graph_type)
        self.sc = Canvas(22, 22, 75)

        self.layout.addWidget(self.select_type)
        self.layout.addWidget(self.sc)
        self.setLayout(self.layout)

        self.exec()

    def graph_show(self, y, x):

        self.sc.axes.clear()
        self.sc.axes.plot(x,y)
        self.sc.draw()

        self.layout.addWidget(self.sc)
        self.setLayout(self.layout)

    def graph_type(self):
        type_date = self.select_type.currentIndex()
        currentDate = arrow.utcnow()

        match type_date:
            case 0:
                connection, cursor = data_base.connect()
                cursor.execute("""SELECT strftime('%Y-%m-%d', time_statistic), value_statistic FROM Statistic 
                                               WHERE id_type_statistic = ?
                                               ORDER BY time_statistic""", (self.type,))
                full_data = cursor.fetchall()
                data_base.close(connection, cursor)

                currentDate = currentDate.format("YYYY-MM")
                self.x = []
                self.y = []
                for one_date in full_data:
                    if one_date[0][:7] == currentDate:
                        if one_date[0] in self.y:
                            index = self.y.index(one_date[0])
                            new = ((self.x[index] + one_date[1])/2)
                            self.x[index] = int(new)

                        else:
                            self.y.append(one_date[0])
                            self.x.append(one_date[1])

                for date in range(len(self.y)):
                    month = calendar.month_abbr[int(self.y[0][-5:-3])]
                    day = self.y[0][8:]
                    self.y.append(f"{day} {month}")
                    self.y.pop(0)

            case 1:
                connection, cursor = data_base.connect()
                cursor.execute("""SELECT strftime('%Y-%m-%d', time_statistic), value_statistic FROM Statistic 
                                                               WHERE id_type_statistic = ?
                                                               ORDER BY time_statistic""", (self.type,))
                data = cursor.fetchall()
                data_base.close(connection, cursor)
                clear_data = []
                currentDate = currentDate.format("YYYY")
                self.x = []
                self.y = []

                for i in data:
                    month = calendar.month_abbr[int(i[0][-5:-3])]
                    year = i[0][:4]
                    clear_data.append([f"{month} {year}", i[1]])

                for one_date in clear_data:
                    if one_date[0][-4:] == currentDate:
                        if one_date[0] in self.y:
                            index = self.y.index(one_date[0])
                            new = ((self.x[index] + one_date[1]) / 2)
                            self.x[index] = int(new)

                        else:
                            self.y.append(one_date[0])
                            self.x.append(one_date[1])

            case 2:
                connection, cursor = data_base.connect()
                cursor.execute("""SELECT strftime('%Y-%m-%d', time_statistic), value_statistic FROM Statistic 
                                                                                   WHERE id_type_statistic = ?
                                                                                   ORDER BY time_statistic""", (self.type,))
                data = cursor.fetchall()
                data_base.close(connection, cursor)
                clear_data = []
                self.x = []
                self.y = []

                for i in data:
                    year = i[0][:4]
                    clear_data.append([f"{year}", i[1]])

                for one_date in clear_data:
                    if one_date[0] in self.y:
                        index = self.y.index(one_date[0])
                        new = ((self.x[index] + one_date[1]) / 2)
                        self.x[index] = int(new)

                    else:
                        self.x.append(one_date[1])
                        self.y.append(one_date[0])


        print(self.x, self.y)
        self.graph_show(self.x, self.y)






