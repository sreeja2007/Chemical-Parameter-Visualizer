import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class ChartGenerator:
    @staticmethod
    def create_pie_chart(data_dict, title="Equipment Type Distribution"):
        fig = Figure(figsize=(6, 4))
        ax = fig.add_subplot(111)
        ax.pie(data_dict.values(), labels=data_dict.keys(), autopct='%1.1f%%', startangle=90)
        ax.set_title(title)
        return fig
    
    @staticmethod
    def create_bar_chart(labels, values, title="Average Flowrate", ylabel="Flowrate"):
        fig = Figure(figsize=(6, 4))
        ax = fig.add_subplot(111)
        ax.bar(labels, values, color='skyblue')
        ax.set_title(title)
        ax.set_ylabel(ylabel)
        ax.set_xlabel("Equipment Type")
        plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')
        fig.tight_layout()
        return fig
    
    @staticmethod
    def create_line_chart(labels, values, title="Pressure & Temperature", ylabel="Value"):
        fig = Figure(figsize=(6, 4))
        ax = fig.add_subplot(111)
        ax.plot(labels, values, marker='o', linestyle='-', color='red')
        ax.set_title(title)
        ax.set_ylabel(ylabel)
        ax.set_xlabel("Metric")
        ax.grid(True, alpha=0.3)
        fig.tight_layout()
        return fig
