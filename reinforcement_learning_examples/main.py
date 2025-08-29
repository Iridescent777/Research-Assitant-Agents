# Example code for Value Iteration
def value_iteration(P, R, gamma=0.9, theta=0.0001):
    """
    P: Transition probabilities of the environment
    R: Rewards
    gamma: Discount factor
    theta: A threshold for deciding when to stop the iteration
    Returns:
    policy: The optimal policy
    V: The value function
    """
    import numpy as np
    num_states = len(R)
    V = np.zeros(num_states)
    policy = np.zeros(num_states, dtype=int)

    while True:
        delta = 0
        for s in range(num_states):
            v = V[s]
            V[s] = max(sum([P[s, a, s1] * (R[s] + gamma * V[s1]) for s1 in range(num_states)]) for a in range(len(P[s])))
            delta = max(delta, abs(v - V[s]))
        if delta < theta:
            break

    for s in range(num_states):
        policy[s] = np.argmax([sum([P[s, a, s1] * (R[s] + gamma * V[s1]) for s1 in range(num_states)]) for a in range(len(P[s]))])

    return policy, V

# Example code for Policy Gradients with a simple neural network
def policy_gradient(env, num_episodes=2000, alpha=0.02):
    """
    env: Environment
    num_episodes: Number of episodes to train on
    alpha: Learning rate
    """
    import numpy as np
    import tensorflow as tf
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense
    from tensorflow.keras.optimizers import Adam

    nA = env.action_space.n

    model = Sequential([
        Dense(24, input_shape=(env.observation_space.shape[0],), activation='relu'),
        Dense(12, activation='relu'),
        Dense(nA, activation='softmax')
    ])
    optimizer = Adam(learning_rate=alpha)

    def choose_action(state):
        state = state[np.newaxis, :]
        probs = model.predict(state)[0]
        return np.random.choice(nA, p=probs)

    returns = []

    for episode in range(num_episodes):
        state = env.reset()
        rewards = []
        actions = []
        states = []

        done = False
        while not done:
            action = choose_action(state)
            next_state, reward, done, _ = env.step(action)
            rewards.append(reward)
            actions.append(action)
            states.append(state)
            state = next_state

        G = np.zeros_like(rewards)
        for t in range(len(rewards)):
            G_sum = 0
            discount = 1
            for k in range(t, len(rewards)):
                G_sum += rewards[k] * discount
                discount *= gamma
            G[t] = G_sum

        actions = np.array(actions)
        states = np.vstack(states)

        with tf.GradientTape() as tape:
            probs = model(states)
            indices = np.array([[i, a] for i, a in enumerate(actions)])
            log_probs = tf.math.log(tf.gather_nd(probs, indices))
            loss = -tf.reduce_mean(log_probs * G)

        grads = tape.gradient(loss, model.trainable_variables)
        optimizer.apply_gradients(zip(grads, model.trainable_variables))

        total_reward = sum(rewards)
        returns.append(total_reward)

    return returns

# Example code for Q-Learning
def q_learning(env, num_episodes=2000, alpha=0.1, gamma=0.99, epsilon=0.1):
    """
    env: Environment
    num_episodes: Number of episodes to train
    alpha: Learning rate
    gamma: Discount factor "y"
    epsilon: Exploration rate
    """
    import numpy as np

    Q = np.zeros((env.observation_space.n, env.action_space.n))

    def choose_action(state):
        if np.random.random() < epsilon:
            return env.action_space.sample()
        return np.argmax(Q[state])

    returns = []

    for episode in range(num_episodes):
        state = env.reset()
        done = False
        total_reward = 0

        while not done:
            action = choose_action(state)
            next_state, reward, done, _ = env.step(action)
            total_reward += reward

            best_next_action = np.argmax(Q[next_state])
            Q[state, action] = Q[state, action] + alpha * (reward + gamma * Q[next_state, best_next_action] - Q[state, action])

            state = next_state

        returns.append(total_reward)

    return returns, Q