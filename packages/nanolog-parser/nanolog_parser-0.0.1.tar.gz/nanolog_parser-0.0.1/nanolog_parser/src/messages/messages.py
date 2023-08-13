from .base_message import BaseMessage
import re


class UnknownMessage(BaseMessage):
    pass


class ConfirmAckMessage(BaseMessage):

    def post_init(self):
        self.vote_type = "final" if self.message["vote"][
            "timestamp"] == 18446744073709551615 else "normal"
        self.vote_count = len(self.message["vote"]["hashes"])
        self.class_name = "ConfirmAckMessage"


class ConfirmAckMessageReceived(ConfirmAckMessage):
    pass


class ConfirmAckMessageSent(ConfirmAckMessage):
    pass


class ConfirmAckMessageDropped(ConfirmAckMessage):
    pass


class ConfirmReqMessage(BaseMessage):
    def post_init(self):
        self.root_count = len(self.message["roots"])
        self.class_name = "ConfirmReqMessage"


class ConfirmReqMessageReceived(ConfirmReqMessage):
    pass


class ConfirmReqMessageSent(ConfirmReqMessage):
    pass


class ConfirmReqMessageDropped(ConfirmReqMessage):
    pass


class PublishMessage(BaseMessage):
    def post_init(self):
        self.class_name = "PublishMessage"


class PublishMessageReceived(PublishMessage):
    pass


class PublishMessageSent(PublishMessage):
    pass


class PublishMessageDropped(PublishMessage):
    pass


class KeepAliveMessage(BaseMessage):
    def post_init(self):
        self.class_name = "KeepAliveMessage"


class KeepAliveMessageReceived(KeepAliveMessage):
    pass


class KeepAliveMessageSent(KeepAliveMessage):
    pass


class KeepAliveMessageDropped(KeepAliveMessage):
    pass


class AscPullAckMessage(BaseMessage):
    def post_init(self):
        self.class_name = "AscPullAckMessage"


class AscPullAckMessageReceived(AscPullAckMessage):
    pass


class AscPullAckMessageSent(AscPullAckMessage):
    pass


class AscPullAckMessageDropped(AscPullAckMessage):
    pass


class AscPullReqMessage(BaseMessage):
    def post_init(self):
        self.class_name = "AscPullReqMessage"


class AscPullReqMessageReceived(AscPullReqMessage):
    pass


class AscPullReqMessageSent(AscPullReqMessage):
    pass


class AscPullReqMessageDropped(AscPullReqMessage):
    pass


class NodeIdHandshakeMessage(BaseMessage):
    def post_init(self):
        self.class_name = "NodeIdHandshakeMessage"


class NodeIdHandshakeMessageReceived(NodeIdHandshakeMessage):
    pass


class NodeIdHandshakeMessageSent(NodeIdHandshakeMessage):
    pass


class NodeIdHandshakeMessageDropped(NodeIdHandshakeMessage):
    pass


class TelemetryReqMessage(BaseMessage):
    def post_init(self):
        self.class_name = "TelemetryReqMessage"


class TelemetryReqMessageReceived(TelemetryReqMessage):
    pass


class TelemetryReqMessageSent(TelemetryReqMessage):
    pass


class TelemetryReqMessageDropped(TelemetryReqMessage):
    pass


class TelemetryAckMessage(BaseMessage):
    def post_init(self):
        self.class_name = "TelemetryAckMessage"


class TelemetryAckMessageReceived(TelemetryReqMessage):
    pass


class TelemetryAckMessageSent(TelemetryReqMessage):
    pass


class TelemetryAckMessageDropped(TelemetryReqMessage):
    pass


class ElectionGenerateVoteNormalMessage(BaseMessage):
    pass


class ElectionGenerateVoteFinalMessage(BaseMessage):
    pass


class ElectionConfirmedMessage(BaseMessage):
    pass


class BroadcastMessage(BaseMessage):
    pass


class FlushMessage(BaseMessage):
    def post_init(self):
        self.root_count = len(self.confirm_req["roots"])


class BlockProcessedMessage(BaseMessage):
    pass


class BlockProcessorMessage(BaseMessage):
    pass


class ActiveStartedMessage(BaseMessage):
    pass


class ActiveStoppedMessage(BaseMessage):
    pass


class ProcessConfirmedMessage(BaseMessage):
    pass


class VoteProcessedMessage(BaseMessage):
    pass


class SendingFrontierMessage(BaseMessage):
    pass


class BulkPullAccountPendingMessage(BaseMessage):
    def post_init(self):
        self.channel = self.connection
        # self.remove_attribute("connection")


class BulkPullAccountMessage(BaseMessage):
    pass


class BulkPullAccountMessageReceived(BulkPullAccountMessage):
    pass


class BulkPullAccountMessageSent(BulkPullAccountMessage):
    pass


class BulkPullAccountMessageDropped(BulkPullAccountMessage):
    pass


class BulkPushMessage(BaseMessage):
    pass


class BulkPushMessageReceived(BulkPushMessage):
    pass


class BulkPushMessageSent(BulkPushMessage):
    pass


class BulkPushMessageDropped(BulkPushMessage):
    pass


class FrontierReqMessage(BaseMessage):
    pass


class FrontierReqMessageReceived(FrontierReqMessage):
    pass


class FrontierReqMessageSent(FrontierReqMessage):
    pass


class FrontierReqMessageDropped(FrontierReqMessage):
    pass


class ProcessedBlocksMessage(BaseMessage):

    def post_init(self):
        self.processed_blocks, self.forced_blocks, self.process_time = self.extract_block_info(
            self.content)

    def extract_block_info(self, message_content):
        match = re.search(
            r'Processed (\d+) blocks \((\d+) forced\) in (\d+) milliseconds',
            message_content)
        if match:
            return int(match.group(1)), int(match.group(2)), int(
                match.group(3))
        else:
            return None, None, None


class BlocksInQueueMessage(BaseMessage):

    def post_init(self):
        self.blocks_in_queue, self.state_blocks, self.forced_blocks = self.extract_block_counts(
            self.content)

    def extract_block_counts(self, message_content):
        match = re.search(
            r'(\d+) blocks \(\+ (\d+) state blocks\) \(\+ (\d+) forced\)',
            message_content)
        if match:
            return int(match.group(1)), int(match.group(2)), int(
                match.group(3))
        else:
            return None, None, None


class VotesProcessedMessage(BaseMessage):

    def post_init(self):
        self.blocks_processed, self.process_duration, self.process_rate = self.extract_block_counts(
            self.content)

    def extract_block_counts(self, message_content):
        match = re.search(
            r'Processed (\d+) votes in (\d+) milliseconds \(rate of (\d+) votes per second\)',
            message_content)
        if match:
            return int(match.group(1)), int(match.group(2)), int(
                match.group(3))
        else:
            return None, None, None
