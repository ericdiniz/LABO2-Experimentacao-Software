QUERY_REPOSITORIES = """
query ($cursor: String) {
  search(query: "language:Java", type: REPOSITORY, first: 100, after: $cursor) {
    pageInfo {
      endCursor
      hasNextPage
    }
    nodes {
      ... on Repository {
        nameWithOwner
        stargazerCount
        forkCount
        url
        createdAt
        releases {
          totalCount
        }
        defaultBranchRef {
          target {
            ... on Commit {
              history(first: 1) {
                totalCount
              }
            }
          }
        }
      }
    }
  }
}
"""
