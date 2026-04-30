import subprocess
from datetime import datetime, timedelta

def get_yesterday_commits():
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    cmd = f'git log --since="{yesterday} 00:00:00" --until="{yesterday} 23:59:59" --pretty=format:"%h - %s"'
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        commits = result.stdout.strip().split("\n") if result.stdout else []
        return commits if commits else ["模拟提交: fix login bug", "模拟提交: update README"]
    except:
        return ["模拟提交: fix login bug", "模拟提交: update README"]

def analyze(commits):
    analysis = {
        "分类": {},
        "高风险": [],
        "日报": ""
    }
    for c in commits:
        if "fix" in c.lower():
            analysis["分类"]["修复"] = analysis["分类"].get("修复", []) + [c]
        elif "feat" in c.lower():
            analysis["分类"]["新功能"] = analysis["分类"].get("新功能", []) + [c]
        else:
            analysis["分类"]["其他"] = analysis["分类"].get("其他", []) + [c]
        if "payment" in c.lower() or "auth" in c.lower():
            analysis["高风险"].append(c)
    analysis["日报"] = f"""
昨日工作摘要：
- 修复：{len(analysis['分类'].get('修复',[]))} 项
- 新功能：{len(analysis['分类'].get('新功能',[]))} 项
- 其他：{len(analysis['分类'].get('其他',[]))} 项
高风险变更：{len(analysis['高风险'])} 项
"""
    return analysis

def main():
    print("=" * 50)
    print("Agent 启动时间:", datetime.now())
    print("获取 Git 记录...")
    commits = get_yesterday_commits()
    print(f"获取到 {len(commits)} 条提交")
    print("执行分析...")
    result = analyze(commits)
    print(result["日报"])
    print("高风险项:", result["高风险"] if result["高风险"] else "无")
    print("模拟 Token 消耗：2150")
    print("=" * 50)

if __name__ == "__main__":
    main()
