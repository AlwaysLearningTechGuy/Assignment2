from app.rate_limiter import RateLimiter

def test_rate_limiter_allows_within_limit():
    rl = RateLimiter(max_requests=3, window_seconds=60)
    assert rl.is_allowed("1.1.1.1")
    assert rl.is_allowed("1.1.1.1")
    assert rl.is_allowed("1.1.1.1")

def test_rate_limiter_blocks_after_limit():
    rl = RateLimiter(max_requests=2, window_seconds=60)
    rl.is_allowed("2.2.2.2")
    rl.is_allowed("2.2.2.2")
    assert rl.is_allowed("2.2.2.2") is False
