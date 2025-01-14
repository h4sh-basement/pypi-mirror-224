import torch
from torch import nn

from spinesTS.layers import Time2Vec
from spinesTS.base import TorchModelMixin


class T2V(nn.Module):
    def __init__(self, in_shapes, out_features, flip_features=False):
        super(T2V, self).__init__()
        self.in_shape_type = type(in_shapes)
        if self.in_shape_type == tuple:
            rows, self.in_features = in_shapes
        else:
            self.in_features, self.out_features = in_shapes, out_features

        self.t2v = Time2Vec(self.in_features)
        if flip_features:
            self.t2v2 = Time2Vec(self.in_features)
            ln_layer_in_fea = 4 * self.in_features
        else:
            ln_layer_in_fea = 2 * self.in_features

        if self.in_shape_type == tuple:
            self.linear = nn.Linear(ln_layer_in_fea * rows, out_features)
        else:
            self.linear = nn.Linear(ln_layer_in_fea, out_features)

        self.flip_features = flip_features

    def forward(self, x):
        x1 = self.t2v(x)
        if self.flip_features:
            _x = x.clone()
            x2 = self.t2v2(torch.flip(_x, dims=[-1]))
            x = torch.concat((x1, x2), dim=-1)
        else:
            x = x1

        if self.in_shape_type == tuple:
            return self.linear(x.reshape(-1, x.shape[1] * x.shape[2]))
        else:
            return self.linear(x)


class Time2VecNet(TorchModelMixin):
    def __init__(self, in_features, out_features, flip_features=False, learning_rate=0.01, random_seed=42, device=None):
        super(Time2VecNet, self).__init__(random_seed, device=device)
        self.in_features, self.out_features = in_features, out_features
        self.learning_rate = learning_rate
        self.flip_features = flip_features
        self.model, self.loss_fn, self.optimizer = self.call()

    def call(self):
        model = T2V(self.in_features, self.out_features, flip_features=self.flip_features)
        loss_fn = nn.HuberLoss()
        optimizer = torch.optim.AdamW(model.parameters(), lr=self.learning_rate)
        return model, loss_fn, optimizer

    def fit(
            self,
            X_train,
            y_train,
            epochs=1000,
            batch_size='auto',
            eval_set=None,
            monitor='val_loss',
            min_delta=0,
            patience=10,
            lr_scheduler='ReduceLROnPlateau',
            lr_scheduler_patience=10,
            lr_factor=0.7,
            restore_best_weights=True,
            verbose=True,
            **kwargs
    ):
        return super().fit(X_train, y_train, epochs, batch_size, eval_set, loss_type='down', metrics_name='mae',
                           monitor=monitor, lr_scheduler=lr_scheduler,
                           lr_scheduler_patience=lr_scheduler_patience,
                           lr_factor=lr_factor,
                           min_delta=min_delta, patience=patience, restore_best_weights=restore_best_weights,
                           verbose=verbose, **kwargs)
