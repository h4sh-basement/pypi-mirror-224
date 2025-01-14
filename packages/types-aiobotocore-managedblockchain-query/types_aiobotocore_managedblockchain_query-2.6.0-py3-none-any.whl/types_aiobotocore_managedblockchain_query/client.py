"""
Type annotations for managedblockchain-query service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_managedblockchain_query/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_managedblockchain_query.client import ManagedBlockchainQueryClient

    session = get_session()
    async with session.create_client("managedblockchain-query") as client:
        client: ManagedBlockchainQueryClient
    ```
"""
import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import QueryNetworkType
from .paginator import (
    ListTokenBalancesPaginator,
    ListTransactionEventsPaginator,
    ListTransactionsPaginator,
)
from .type_defs import (
    BatchGetTokenBalanceInputItemTypeDef,
    BatchGetTokenBalanceOutputTypeDef,
    BlockchainInstantTypeDef,
    GetTokenBalanceOutputTypeDef,
    GetTransactionOutputTypeDef,
    ListTokenBalancesOutputTypeDef,
    ListTransactionEventsOutputTypeDef,
    ListTransactionsOutputTypeDef,
    ListTransactionsSortTypeDef,
    OwnerFilterTypeDef,
    OwnerIdentifierTypeDef,
    TokenFilterTypeDef,
    TokenIdentifierTypeDef,
)

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ManagedBlockchainQueryClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class ManagedBlockchainQueryClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_managedblockchain_query/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ManagedBlockchainQueryClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_managedblockchain_query/client/#exceptions)
        """

    async def batch_get_token_balance(
        self, *, getTokenBalanceInputs: Sequence[BatchGetTokenBalanceInputItemTypeDef] = ...
    ) -> BatchGetTokenBalanceOutputTypeDef:
        """
        Gets the token balance for a batch of tokens by using the `GetTokenBalance`
        action for every token in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.batch_get_token_balance)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_managedblockchain_query/client/#batch_get_token_balance)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_managedblockchain_query/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_managedblockchain_query/client/#close)
        """

    async def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_managedblockchain_query/client/#generate_presigned_url)
        """

    async def get_token_balance(
        self,
        *,
        tokenIdentifier: TokenIdentifierTypeDef,
        ownerIdentifier: OwnerIdentifierTypeDef,
        atBlockchainInstant: BlockchainInstantTypeDef = ...
    ) -> GetTokenBalanceOutputTypeDef:
        """
        Gets the balance of a specific token, including native tokens, for a given
        address (wallet or contract) on the blockchain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.get_token_balance)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_managedblockchain_query/client/#get_token_balance)
        """

    async def get_transaction(
        self, *, transactionHash: str, network: QueryNetworkType
    ) -> GetTransactionOutputTypeDef:
        """
        Get the details of a transaction.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.get_transaction)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_managedblockchain_query/client/#get_transaction)
        """

    async def list_token_balances(
        self,
        *,
        tokenFilter: TokenFilterTypeDef,
        ownerFilter: OwnerFilterTypeDef = ...,
        nextToken: str = ...,
        maxResults: int = ...
    ) -> ListTokenBalancesOutputTypeDef:
        """
        This action returns the following for a given a blockchain network: * Lists all
        token balances owned by an address (either a contact address or a wallet
        address).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.list_token_balances)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_managedblockchain_query/client/#list_token_balances)
        """

    async def list_transaction_events(
        self,
        *,
        transactionHash: str,
        network: QueryNetworkType,
        nextToken: str = ...,
        maxResults: int = ...
    ) -> ListTransactionEventsOutputTypeDef:
        """
        An array of `TransactionEvent` objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.list_transaction_events)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_managedblockchain_query/client/#list_transaction_events)
        """

    async def list_transactions(
        self,
        *,
        address: str,
        network: QueryNetworkType,
        fromBlockchainInstant: BlockchainInstantTypeDef = ...,
        toBlockchainInstant: BlockchainInstantTypeDef = ...,
        sort: ListTransactionsSortTypeDef = ...,
        nextToken: str = ...,
        maxResults: int = ...
    ) -> ListTransactionsOutputTypeDef:
        """
        Lists all of the transactions on a given wallet address or to a specific
        contract.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.list_transactions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_managedblockchain_query/client/#list_transactions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_token_balances"]
    ) -> ListTokenBalancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_managedblockchain_query/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_transaction_events"]
    ) -> ListTransactionEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_managedblockchain_query/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_transactions"]
    ) -> ListTransactionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_managedblockchain_query/client/#get_paginator)
        """

    async def __aenter__(self) -> "ManagedBlockchainQueryClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_managedblockchain_query/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_managedblockchain_query/client/)
        """
