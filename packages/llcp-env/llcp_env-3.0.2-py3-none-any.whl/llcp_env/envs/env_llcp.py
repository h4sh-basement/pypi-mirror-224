import sys
import numpy as np
from gym import Env, spaces
import time

# from gym.envs.toy_text.utils import categorical_sample
# dic_clfs1 = np.load('dic_clfs.npy', allow_pickle=True).item()

#
# X_train = dic_clfs1['xl2']
# Y_train = dic_clfs1['yl2']
# X_val = dic_clfs1['xl2']
# y_val = dic_clfs1['yl3']

class CPEnv(Env):
    print("正在搭建初始环境811")
    print("文件位置：", sys.argv[0])
    # dic_clfs1 = np.load('dic_env.npy', allow_pickle=True).item()
    dic_clfs1 = np.load('/content/drive/MyDrive/Colab Notebooks/dic_clfs_0614_local.npy', allow_pickle=True).item()
    print(dic_clfs1['xl2'].shape, dic_clfs1['yl2'].shape, dic_clfs1['xl3'].shape, dic_clfs1['yl3'].shape)
    # print(dic_clfs1['tx'].shape, dic_clfs1['ty'].shape)

    metadata = {'render.modes': ['human']}

    def __init__(self):

        self.hangshu = 1

        self.X_train = np.load('/content/drive/MyDrive/Colab Notebooks/dic_clfs_0614_local.npy', allow_pickle=True).item()['xl2']
        self.y_train = np.load('/content/drive/MyDrive/Colab Notebooks/dic_clfs_0614_local.npy', allow_pickle=True).item()['yl2']

        # self.X_train = np.load('/content/drive/MyDrive/Colab Notebooks/dic_clfs1.npy', allow_pickle=True).item()['tx']
        # self.y_train = np.load('/content/drive/MyDrive/Colab Notebooks/dic_clfs1.npy', allow_pickle=True).item()['ty']

        # self.X_train = np.load('dic_clfs1.npy', allow_pickle=True).item()['tx']
        self.X_train = self.X_train.reshape(self.X_train.shape[0],self.X_train.shape[1])
        # self.y_train = np.load('dic_clfs1.npy', allow_pickle=True).item()['ty']

        # print(self.X_train.shape)
        # self.X_val = np.load('dic_clfs.npy', allow_pickle=True).item()['xl3']
        # self.y_val = np.load('dic_clfs.npy', allow_pickle=True).item()['yl3']

        self.observation_space = spaces.Box(0,1, shape=(self.X_train.shape[1],),dtype=np.float64)
        # self.observation_space = spaces.Box(low=0, high=1, shape=(1, self.X_train.shape[1]), dtype=np.float32)
        # print("self.observation_space=", self.observation_space)
        self.action_space = spaces.Discrete(2)
        # self.action_space = spaces.MultiDiscrete([2] * self.hangshu)

        # self.state = None
        # self.dataset = list(zip(self.X_train, self.y_train))

    def reset(self):
        self.jishu = 0
        self.score = 0
        self.right_nums = 0

        # 打乱顺序

        num = time.time()
        snd = float(str(num).split(".")[1])
        snd = int(snd)
        # print("此次种子为：",snd)
        self.shunxu = np.arange(0, self.X_train.shape[0])
        # print(self.shunxu)
        np.random.seed(snd)
        np.random.shuffle(self.shunxu)
        # print(self.shunxu)
        self.X_train = self.X_train[self.shunxu]
        self.y_train = self.y_train[self.shunxu]
        self.state = self.X_train[self.jishu]
        self.true_value = self.y_train[self.jishu]
        self.jishu = self.jishu + 1

        # 此次种子为： 940769
        # [0     1     2... 30997 30998 30999]
        # [27214  8037 11191... 30095 20848 13066]

        # np.random.seed(seed)
        # np.random.shuffle(self.X_train)
        # np.random.seed(seed)
        # np.random.shuffle(self.y_train)
        # tf.random.set_seed(seed)

        # self.state = self.X_train[self.jishu]
        # self.true_value = self.y_train[self.jishu]
        # self.jishu = self.jishu + 1

        if self.true_value == 1:
            # print(self.true_value)
            self.right_nums = 1
        else:
            # print(self.true_value)
            self.right_nums = 0

        return self.state

    def step(self, action):

        # Calculate the prediction
        # prediction = np.mean(self.state[action])
        # print(prediction)
        # print("a",action)
        # print(self.true_value)
        # prediction = action

        done = 0
        self.reward = 0
        self.score = 0
        self.wrong_score = 0

        ##以200个位一组，结束后done为0
        self.every_zu_nums = 200
        yushu = self.jishu % self.every_zu_nums
        # print("余数：", yushu)
        if yushu == 0:
            done = 1
        else:
            done = 0

        if self.true_value == 1:
            # print("self.true_value=",self.true_value)
            self.right_nums = 1
            if action == 1:
                # print("action=1")
                self.reward = 20
                self.score = 1
                self.wrong_score = 0
            else:
                # print("action=buwei1")
                self.reward = -20
                self.score = 0
                self.wrong_score = 0
        elif self.true_value == 0:
            # print("self.true_value=",self.true_value)
            self.right_nums = 0

            if action == 1:
                # print("action=1")
                self.reward = -20
                self.score = 0
                self.wrong_score = 1
            else:
                # print("action=buwei1")
                self.reward = -10
                self.score = 0
                self.wrong_score = 0
        else:
            print("本组数据有问题，非0非1")

        # reward
        # Calculate the reward
        # if action == 1:
        #     if self.true_value == 1:
        #         reward = 1
        #         self.score = 1
        #     else:
        #         reward = -1
        #         self.score = 0

        # elif prediction == 0:
        #     if prediction == self.true_value:
        #         reward = 0.5
        #     else:
        #         reward = 0
        # else:
        #     reward = 0

        # next state
        self.state = self.X_train[self.jishu]
        self.true_value = self.y_train[self.jishu]
        self.jishu = self.jishu + 1

        info = {}
        info['score'] = self.score
        info['right_nums'] = self.right_nums
        info['wrong_score'] = self.wrong_score

        # print("one step is over")
        # print(type(self.state))
        return self.state, self.reward, done, info

    def render(self, mode='human'):
        print("Ground truth: ", self.y_train[self.jishu])
        # print("Predictions: ", predictions)





