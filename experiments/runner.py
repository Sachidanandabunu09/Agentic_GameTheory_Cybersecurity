"""Run one episode of (environment, policy). Returns list of per-round step dicts."""

def run_episode(env, policy, seed):
    obs = env.reset(seed)
    policy.reset(seed)
    rows = []
    while True:
        j = policy.act(obs, true_threat=env.true_threat())
        info = env.step(j)
        policy.update(info)
        rows.append(info)
        obs = info["observation"]
        if info["done"]:
            return rows
