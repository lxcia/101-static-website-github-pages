import plotly.graph_objects as go
import numpy as np
import plotly.io as pio
import ipywidgets as widgets
from ipywidgets import interact
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import numpy as np
import plotly

# Set the default template to 'plotly'
pio.templates.default = 'plotly'

# Define location names
location1 = "Clarke County, GA"
location2 = "Forsyth County, GA"
location3 = "DeKalb County, GA"

# Define location endpoints
location1_end = -0.166
location2_end = 0.251
location3_end = 0.323

# Define line start and end coordinates for each line
line1start_x = -1
line1end_x = location2_end
line2start_x = -1
line2end_x = location1_end
line3start_x = -1
line3end_x = location3_end

# Define maternal morbidity rates
location1_morbidity = "2.82% 🟥 🟥 🟥"
location2_morbidity = "0.89% 🟥"
location3_morbidity = "0.79% 🟥"

# Define infant abnormality rates
location1_abnormality = "13.6%"
location2_abnormality = "14.5%"
location3_abnormality = "29.3%"

# Generate straight line data for each line
N = 15
xx1 = np.linspace(line1start_x, line1end_x, N)
xx2 = np.linspace(line2start_x, line2end_x, N)
xx3 = np.linspace(line3start_x, line3end_x, N)

yy1 = np.zeros(N)
yy2 = np.full(N, 0.5)
yy3 = np.linspace(-0.5, -0.5, N)

loop1 = 1
loop2 = 4
loop3 = 2

def generateFrames(loop1, loop2, loop3):
    # init result
    frames = []

    # outer loop to keep going

    while loop1 > 0 or loop2 > 0 or loop3 > 0:

        # frames when all the loops need to move forward
        if loop1 > 0 and loop2 > 0 and loop3 > 0:
            print("first step")
            forward_frames1 = [
                go.Frame(
                    data=[
                        go.Scatter(x=xx1[:k + 1], y=yy1[:k + 1], mode="lines", line=dict(width=2, color="#c39999"),
                                   showlegend=False),
                        go.Scatter(x=xx2[:k + 1], y=yy2[:k + 1], mode="lines", line=dict(width=2, color="#c39999"),
                                   showlegend=False),
                        go.Scatter(x=xx3[:k + 1], y=yy3[:k + 1], mode="lines", line=dict(width=2, color="#c39999"),
                                   showlegend=False),
                        go.Scatter(x=[xx1[k]], y=[yy1[k]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                        go.Scatter(x=[xx2[k]], y=[yy2[k]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                        go.Scatter(x=[xx3[k]], y=[yy3[k]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                    ],
                    name=f"forward_frame1{k}"
                )
                for k in range(N)
            ]

            frames += forward_frames1

            backward_frames1 = [
                go.Frame(
                    data=[
                        go.Scatter(x=np.concatenate((xx1[:k], xx1[-1:])), y=yy1[:k].tolist() + [yy1[-1]], mode="lines",
                                   line=dict(width=2, color="#c39999")),
                        go.Scatter(x=np.concatenate((xx2[:k], xx2[-1:])), y=yy2[:k].tolist() + [yy2[-1]], mode="lines",
                                   line=dict(width=2, color="#c39999")),
                        go.Scatter(x=np.concatenate((xx3[:k], xx3[-1:])), y=yy3[:k].tolist() + [yy3[-1]], mode="lines",
                                   line=dict(width=2, color="#c39999")),
                        go.Scatter(x=[xx1[k - 1]], y=[yy1[k - 1]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                        go.Scatter(x=[xx2[k - 1]], y=[yy2[k - 1]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                        go.Scatter(x=[xx3[k - 1]], y=[yy3[k - 1]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                    ],
                    name=f"backward_frame1{k}"
                )
                for k in range(N - 1, 0, -1)
            ]
            frames += backward_frames1
            loop1 -= 1
            loop2 -= 1
            loop3 -= 1

        # frames when ONLY LOOP 1 moves
        if loop1 > 0 and loop2 == 0 and loop3 == 0:
            forward_frames2 = [
                go.Frame(
                    data=[
                        # Stationary blue line
                        go.Scatter(x=xx1, y=yy1, mode="lines", line=dict(width=2, color="#c39999"), showlegend=False),
                        # Animated green line
                        go.Scatter(x=xx2[:k + 1], y=yy2[:k + 1], mode="lines", line=dict(width=2, color="#c39999"),
                                   showlegend=False),
                        # Stationary red line
                        go.Scatter(x=xx3, y=yy3, mode="lines", line=dict(width=2, color="#c39999"), showlegend=False),
                        # Stationary blue point
                        go.Scatter(x=[xx1[0]], y=[yy1[0]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                        # Animated green point
                        go.Scatter(x=[xx2[k]], y=[yy2[k]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                        # Stationary red point
                        go.Scatter(x=[xx3[0]], y=[yy3[0]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                    ],
                    name=f"forward_frame2{k}"
                )
                for k in range(N)
            ]
            frames += forward_frames2

            backward_frames2 = [
                go.Frame(
                    data=[
                        # Stationary blue line
                        go.Scatter(x=xx1, y=yy1, mode="lines", line=dict(width=2, color="#c39999")),
                        # Animated green line
                        go.Scatter(x=np.concatenate((xx2[:k], xx2[-1:])), y=yy2[:k].tolist() + [yy2[-1]], mode="lines",
                                   line=dict(width=2, color="#c39999")),
                        # Stationary red line
                        go.Scatter(x=xx3, y=yy3, mode="lines", line=dict(width=2, color="#c39999")),
                        # Stationary blue point
                        go.Scatter(x=[xx1[0]], y=[yy1[0]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                        # Animated green point
                        go.Scatter(x=[xx2[k - 1]], y=[yy2[k - 1]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                        # Stationary red point
                        go.Scatter(x=[xx3[0]], y=[yy3[0]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                    ],
                    name=f"backward_frame2{k}"
                )
                for k in range(N - 1, 0, -1)
            ]
            frames += backward_frames2
            loop1 -= 1

        # frames when ONLY LOOP 2 moves
        if loop1 == 0 and loop2 > 0 and loop3 == 0:
            forward_frames3 = [
                go.Frame(
                    data=[
                        # Animated blue line
                        go.Scatter(x=xx1[:k + 1], y=yy1[:k + 1], mode="lines", line=dict(width=2, color="#c39999"),
                                   showlegend=False),
                        # Stationary green line
                        go.Scatter(x=xx2, y=yy2, mode="lines", line=dict(width=2, color="#c39999"), showlegend=False),
                        # Stationary red line
                        go.Scatter(x=xx3, y=yy3, mode="lines", line=dict(width=2, color="#c39999"), showlegend=False),
                        # Animated blue point
                        go.Scatter(x=[xx1[k]], y=[yy1[k]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                        # Stationary green point
                        go.Scatter(x=[xx2[0]], y=[yy2[0]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                        # Stationary red point
                        go.Scatter(x=[xx3[0]], y=[yy3[0]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                    ],
                    name=f"forward_frame3{k}"
                )
                for k in range(N)
            ]
            frames += forward_frames3

            backward_frames3 = [
                go.Frame(
                    data=[
                        # Animated blue line
                        go.Scatter(x=np.concatenate((xx1[:k], xx1[-1:])), y=yy1[:k].tolist() + [yy1[-1]], mode="lines",
                                   line=dict(width=2, color="#c39999")),
                        # Stationary green line
                        go.Scatter(x=xx2, y=yy2, mode="lines", line=dict(width=2, color="#c39999")),
                        # Stationary red line
                        go.Scatter(x=xx3, y=yy3, mode="lines", line=dict(width=2, color="#c39999")),
                        # Animated blue point
                        go.Scatter(x=[xx1[k - 1]], y=[yy1[k - 1]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                        # Stationary green point
                        go.Scatter(x=[xx2[0]], y=[yy2[0]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                        # Stationary red point
                        go.Scatter(x=[xx3[0]], y=[yy3[0]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                    ],
                    name=f"backward_frame3{k}"
                )
                for k in range(N - 1, 0, -1)
            ]
            frames += backward_frames3
            loop2 -= 1

        # frames when ONLY LOOP 3 moves
        if loop1 == 0 and loop2 == 0 and loop3 > 0:
            forward_frames4 = [
                go.Frame(
                    data=[
                        # Stationary blue line
                        go.Scatter(x=xx1, y=yy1, mode="lines", line=dict(width=2, color="#c39999"), showlegend=False),
                        # Stationary green line
                        go.Scatter(x=xx2, y=yy2, mode="lines", line=dict(width=2, color="#c39999"), showlegend=False),
                        # Animated red line
                        go.Scatter(x=xx3[:k + 1], y=yy3[:k + 1], mode="lines", line=dict(width=2, color="#c39999"),
                                   showlegend=False),
                        # Stationary blue point
                        go.Scatter(x=[xx1[0]], y=[yy1[0]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                        # Stationary green point
                        go.Scatter(x=[xx2[0]], y=[yy2[0]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                        # Animated red point
                        go.Scatter(x=[xx3[k]], y=[yy3[k]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                    ],
                    name=f"forward_frame4{k}"
                )
                for k in range(N)
            ]
            frames += forward_frames4

            backward_frames4 = [
                go.Frame(
                    data=[
                        # Stationary blue line
                        go.Scatter(x=xx1, y=yy1, mode="lines", line=dict(width=2, color="#c39999")),
                        # Stationary green line
                        go.Scatter(x=xx2, y=yy2, mode="lines", line=dict(width=2, color="#c39999")),
                        # Animated red line
                        go.Scatter(x=np.concatenate((xx3[:k], xx3[-1:])), y=yy3[:k].tolist() + [yy3[-1]], mode="lines",
                                   line=dict(width=2, color="#c39999")),
                        # Stationary blue point
                        go.Scatter(x=[xx1[0]], y=[yy1[0]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                        # Stationary green point
                        go.Scatter(x=[xx2[0]], y=[yy2[0]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                        # Animated red point
                        go.Scatter(x=[xx3[k - 1]], y=[yy3[k - 1]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                    ],
                    name=f"backward_frame4{k}"
                )
                for k in range(N - 1, 0, -1)
            ]
            frames += backward_frames4
            loop3 -= 1

            # CASE OF LOOP 1 and LOOP 3
        if loop1 > 0 and loop2 == 0 and loop3 > 0:
            forward_frames5 = [
                go.Frame(
                    data=[
                        go.Scatter(x=xx1, y=yy1, mode="lines", line=dict(width=2, color="#c39999"), showlegend=False),
                        go.Scatter(x=xx2[:k + 1], y=yy2[:k + 1], mode="lines", line=dict(width=2, color="#c39999"),
                                   showlegend=False),
                        go.Scatter(x=xx3[:k + 1], y=yy3[:k + 1], mode="lines", line=dict(width=2, color="#c39999"),
                                   showlegend=False),
                        go.Scatter(x=[xx1[0]], y=[yy1[0]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                        go.Scatter(x=[xx2[k]], y=[yy2[k]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                        go.Scatter(x=[xx3[k]], y=[yy3[k]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                    ],
                    name=f"forward_frame5{k}"
                )
                for k in range(N)
            ]

            frames += forward_frames5

            backward_frames5 = [
                go.Frame(
                    data=[
                        # Stationary blue line
                        go.Scatter(x=xx1, y=yy1, mode="lines", line=dict(width=2, color="#c39999")),
                        go.Scatter(x=np.concatenate((xx2[:k], xx2[-1:])), y=yy2[:k].tolist() + [yy2[-1]], mode="lines",
                                   line=dict(width=2, color="#c39999")),
                        go.Scatter(x=np.concatenate((xx3[:k], xx3[-1:])), y=yy3[:k].tolist() + [yy3[-1]], mode="lines",
                                   line=dict(width=2, color="#c39999")),
                        # Stationary blue point
                        go.Scatter(x=[xx1[0]], y=[yy1[0]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                        go.Scatter(x=[xx2[k - 1]], y=[yy2[k - 1]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                        go.Scatter(x=[xx3[k - 1]], y=[yy3[k - 1]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                    ],
                    name=f"backward_frame5{k}"
                )
                for k in range(N - 1, 0, -1)
            ]
            frames += backward_frames5
            loop1 -= 1
            loop3 -= 1

        # CASE OF LOOP 1 AND LOOP 2 (GREEN AND BLUE)

        if loop1 > 0 and loop2 > 0 and loop3 == 0:
            forward_frames6 = [
                go.Frame(
                    data=[
                        go.Scatter(x=xx1[:k + 1], y=yy1[:k + 1], mode="lines", line=dict(width=2, color="#c39999"),
                                   showlegend=False),
                        go.Scatter(x=xx2[:k + 1], y=yy2[:k + 1], mode="lines", line=dict(width=2, color="#c39999"),
                                   showlegend=False),
                        # Stationary red line
                        go.Scatter(x=xx3, y=yy3, mode="lines", line=dict(width=2, color="#c39999"), showlegend=False),
                        go.Scatter(x=[xx1[k]], y=[yy1[k]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                        go.Scatter(x=[xx2[k]], y=[yy2[k]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                        # Stationary red point
                        go.Scatter(x=[xx3[0]], y=[yy3[0]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                    ],
                    name=f"forward_frame6{k}"
                )
                for k in range(N)
            ]

            frames += forward_frames6

            backward_frames6 = [
                go.Frame(
                    data=[
                        go.Scatter(x=np.concatenate((xx1[:k], xx1[-1:])), y=yy1[:k].tolist() + [yy1[-1]], mode="lines",
                                   line=dict(width=2, color="#c39999")),
                        go.Scatter(x=np.concatenate((xx2[:k], xx2[-1:])), y=yy2[:k].tolist() + [yy2[-1]], mode="lines",
                                   line=dict(width=2, color="#c39999")),
                        # Stationary red line
                        go.Scatter(x=xx3, y=yy3, mode="lines", line=dict(width=2, color="#c39999")),
                        go.Scatter(x=[xx1[k - 1]], y=[yy1[k - 1]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                        go.Scatter(x=[xx2[k - 1]], y=[yy2[k - 1]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                        # Stationary red point
                        go.Scatter(x=[xx3[0]], y=[yy3[0]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                    ],
                    name=f"backward_frame6{k}"
                )
                for k in range(N - 1, 0, -1)
            ]
            frames += backward_frames6
            loop1 -= 1
            loop2 -= 1

        # CASE OF LOOP 2 AND LOOP 3 (BLUE AND RED)
        if loop1 == 0 and loop2 > 0 and loop3 > 0:
            forward_frames7 = [
                go.Frame(
                    data=[
                        go.Scatter(x=xx1[:k + 1], y=yy1[:k + 1], mode="lines", line=dict(width=2, color="#c39999"),
                                   showlegend=False),
                        # Stationary green line
                        go.Scatter(x=xx2, y=yy2, mode="lines", line=dict(width=2, color="#c39999"), showlegend=False),
                        go.Scatter(x=xx3[:k + 1], y=yy3[:k + 1], mode="lines", line=dict(width=2, color="#c39999"),
                                   showlegend=False),
                        go.Scatter(x=[xx1[k]], y=[yy1[k]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                        # Stationary green point
                        go.Scatter(x=[xx2[0]], y=[yy2[0]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                        go.Scatter(x=[xx3[k]], y=[yy3[k]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                    ],
                    name=f"forward_frame7{k}"
                )
                for k in range(N)
            ]

            frames += forward_frames7

            backward_frames7 = [
                go.Frame(
                    data=[
                        go.Scatter(x=np.concatenate((xx1[:k], xx1[-1:])), y=yy1[:k].tolist() + [yy1[-1]], mode="lines",
                                   line=dict(width=2, color="#c39999")),
                        # Stationary green line
                        go.Scatter(x=xx2, y=yy2, mode="lines", line=dict(width=2, color="#c39999")),
                        go.Scatter(x=np.concatenate((xx3[:k], xx3[-1:])), y=yy3[:k].tolist() + [yy3[-1]], mode="lines",
                                   line=dict(width=2, color="#c39999")),
                        go.Scatter(x=[xx1[k - 1]], y=[yy1[k - 1]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                        # Stationary green point
                        go.Scatter(x=[xx2[0]], y=[yy2[0]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                        go.Scatter(x=[xx3[k - 1]], y=[yy3[k - 1]], mode="text", text="🤰", showlegend=False,
                                   textfont=dict(size=30)),
                    ],
                    name=f"backward_frame7{k}"
                )
                for k in range(N - 1, 0, -1)
            ]
            frames += backward_frames7
            loop2 -= 1
            loop3 -= 1

    # final_frame = go.Frame(
    #     data=[
    #         go.Scatter(x=xx1, y=yy1, mode="lines", line=dict(width=2, color="#c39999"), showlegend=False),
    #         go.Scatter(x=xx2, y=yy2, mode="lines", line=dict(width=2, color="#c39999"), showlegend=False),
    #         go.Scatter(x=xx3, y=yy3, mode="lines", line=dict(width=2, color="#c39999"), showlegend=False),
    #         # Add your additional static content (text, lines, etc.) for the final frame
    #         go.Scatter(x=[-0.22], y=[0.05], mode="text",
    #                    text="👶 Abnormality Rate: " + location1_abnormality + ", 🤰 Morbidity Rate: " + location1_morbidity,
    #                    showlegend=False, textfont=dict(size=13, color="#c39999", family="Roboto, sans-serif")),
    #         go.Scatter(x=[-0.22], y=[0.55], mode="text",
    #                    text="👶 Abnormality Rate: " + location2_abnormality + ", 🤰 Morbidity Rate: " + location2_morbidity,
    #                    showlegend=False, textfont=dict(size=13, color="#c39999", family="Roboto, sans-serif")),
    #         go.Scatter(x=[-0.22], y=[-0.45], mode="text",
    #                    text="👶 Abnormality Rate: " + location3_abnormality + ", 🤰 Morbidity Rate: " + location3_morbidity,
    #                    showlegend=False, textfont=dict(size=13, color="#c39999", family="Roboto, sans-serif")),
    #     ],
    #     name="final_frame"
    # )
    #
    # frames += [final_frame]

    # previous_frame = go.Frame(
    #     data=[
    #         go.Scatter(x=xx1, y=yy1, mode="lines", line=dict(width=2, color="#c39999"), showlegend=False),
    #         go.Scatter(x=xx2, y=yy2, mode="lines", line=dict(width=2, color="#c39999"), showlegend=False),
    #         go.Scatter(x=xx3, y=yy3, mode="lines", line=dict(width=2, color="#c39999"), showlegend=False),
    #         go.Scatter(x=[-0.22], y=[0.05], mode="text",
    #                    text="👶 Abnormality Rate: " + location1_abnormality + ", 🤰 Morbidity Rate: " + location1_morbidity,
    #                    showlegend=False, textfont=dict(size=13, color="#c39999", family="Roboto, sans-serif"),
    #                    visible=False),
    #         go.Scatter(x=[-0.22], y=[0.55], mode="text",
    #                    text="👶 Abnormality Rate: " + location2_abnormality + ", 🤰 Morbidity Rate: " + location2_morbidity,
    #                    showlegend=False, textfont=dict(size=13, color="#c39999", family="Roboto, sans-serif"),
    #                    visible=False),
    #         go.Scatter(x=[-0.22], y=[-0.45], mode="text",
    #                    text="👶 Abnormality Rate: " + location3_abnormality + ", 🤰 Morbidity Rate: " + location3_morbidity,
    #                    showlegend=False, textfont=dict(size=13, color="#c39999", family="Roboto, sans-serif"),
    #                    visible=False),
    #     ],
    #     name="previous_frame"
    # )

    final_frame = go.Frame(
        data=[
            go.Scatter(x=xx1, y=yy1, mode="lines", line=dict(width=2, color="#c39999"), showlegend=False),
            go.Scatter(x=xx2, y=yy2, mode="lines", line=dict(width=2, color="#c39999"), showlegend=False),
            go.Scatter(x=xx3, y=yy3, mode="lines", line=dict(width=2, color="#c39999"), showlegend=False),
            # prev: x=[-0.22], y=[0.05]
            go.Scatter(x=[-0.48], y=[0.05], mode="text",
                       text="🤰 <b> Morbidity Rate: </b>" + location1_morbidity,
                       showlegend=False, textfont=dict(size=13, color="#c39999", family="Roboto, sans-serif"),
                       visible=True),
            go.Scatter(x=[-0.58], y=[0.55], mode="text",
                       text="🤰 <b> Morbidity Rate: </b>" + location2_morbidity,
                       showlegend=False, textfont=dict(size=13, color="#c39999", family="Roboto, sans-serif"),
                       visible=True),
            go.Scatter(x=[-0.58], y=[-0.45], mode="text",
                       text="🤰 <b> Morbidity Rate: </b>" + location3_morbidity,
                       showlegend=False, textfont=dict(size=13, color="#c39999", family="Roboto, sans-serif"),
                       visible=True),
        ],
        name="final_frame"
    )

    frames += [final_frame]

    return frames

fig = go.Figure(
        data=[
            go.Scatter(x=xx1, y=yy1, mode="lines", line=dict(width=2, color="#c39999"), showlegend=False),
            go.Scatter(x=xx2, y=yy2, mode="lines", line=dict(width=2, color="#c39999"), showlegend=False),
            go.Scatter(x=xx3, y=yy3, mode="lines", line=dict(width=2, color="#c39999"), showlegend=False),
            go.Scatter(x=[xx1[0]], y=[yy1[0]], mode="text", text="🤰", showlegend=False, textfont=dict(size=30)),
            go.Scatter(x=[xx2[0]], y=[yy2[0]], mode="text", text="🤰", showlegend=False, textfont=dict(size=30)),
            go.Scatter(x=[xx3[0]], y=[yy3[0]], mode="text", text="🤰", showlegend=False, textfont=dict(size=30)),
        ],
        layout=go.Layout(
            xaxis=dict(range=[-2, 3], autorange=False, zeroline=False, showgrid=False, visible=False),
            yaxis=dict(range=[-1, 1], autorange=False, zeroline=False, showgrid=False, visible=False),
            title=dict(
                text="Clinic Access and Prenatal Care - Georgia",
                font=dict(size=17, color="#c39999", family="Roboto, sans-serif"),
                x=0.05,  # Move the title slightly to the right
                y=0.85,  # Move the title slightly down
            ),
            hovermode=False,
            updatemenus=[
                dict(
                    type="buttons",
                    buttons=[
                        dict(
                            label="Play",
                            method="animate",
                            args=[None],
                        )
                    ],
                    x=0.45,  # Adjust the x-coordinate for the entire button group
                    y=1.1,  # Adjust the y-coordinate for the entire button group
                    font=dict(
                                family="Roboto, sans-serif",  # Set the font family
                                size=14,         # Set the font size
                                color="#c39999"  # Set the font color
                            )
                )
            ],

            plot_bgcolor='#fff0f0',  # Set background color to transparent
            paper_bgcolor='#fff0f0',  # Set paper (plot area) background color to transparent
            width=1000,  # Set the width of the chart to 800 pixels
            height=400,  # Set the height of the chart to 600 pixels
            margin=dict(t=80, b=10, l=10, r=10),  # Set the margins for top, bottom, left, and right
            # Add a text annotation at the specified coordinates
            # Add a text annotation at the specified coordinates
            annotations=[
                dict(
                    text=location1,
                    x=-1.53,  # X-coordinate
                    y=0.52,  # Y-coordinate
                    showarrow=False,
                    font=dict(size=13, color="#c39999", family="Roboto, sans-serif"),
                ),
                dict(
                    text=location3,
                    x=-1.53,  # X-coordinate
                    y=-0.48,  # Y-coordinate
                    showarrow=False,
                    font=dict(size=13, color="#c39999", family="Roboto, sans-serif"),
                ),
                dict(
                    text=location2,
                    x=-1.55,  # X-coordinate
                    y=0.02,  # Y-coordinate
                    showarrow=False,
                    font=dict(size=13, color="#c39999", family="Roboto, sans-serif"),
                ),
                dict(  # location 1 hospital
                    text="🏥",
                    x=location1_end + 0.15,  # X-coordinate
                    y=0.6,  # Y-coordinate
                    showarrow=False,
                    font=dict(size=35),
                ),
                dict(  # location 2 hospital
                    text="🏥",
                    x=location2_end + 0.15,  # X-coordinate
                    y=0.1,  # Y-coordinate
                    showarrow=False,
                    font=dict(size=35),
                ),
                dict(  # location 3 hospital
                    text="🏥",
                    x=location3_end + 0.15,  # X-coordinate
                    y=-0.405,  # Y-coordinate
                    showarrow=False,
                    font=dict(size=35),
                )
            ],
        )
    )

fig.frames = generateFrames(loop1, loop2, loop3)

# Update animation settings
animation_settings = dict(
        frame=dict(duration=100, redraw=True),
        fromcurrent=False,
)
fig.update_layout(updatemenus=[dict(type="buttons", showactive=False, buttons=[dict(label="Play",
                                                                                        method="animate",
                                                                                        args=[None, animation_settings])])])

fig.show(config={'displayModeBar': False})
#
# # Save the animation as an HTML file
# fig.write_html("animationhtml44.html")


# Generate frames
# fig.frames = generateFrames(loop1, loop2, loop3)

plotly.offline.plot(fig, auto_play=False, config={'displayModeBar': False})

# # Save the animation as an HTML file
# fig.write_html("animationhtml44.html")