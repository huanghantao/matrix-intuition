.PHONY: setup test check figures book

setup:
	pip install -r requirements.txt

# 跑你战场上的测试（一开始全是红：TODO 未实现，正常的）
test:
	pytest tests

# 跑参考答案的测试（应该全绿）
check:
	IMPL=reference pytest tests

# 重新生成所有配图
figures:
	python figures/gen_all.py

# 构建 mdBook
book:
	mdbook build
